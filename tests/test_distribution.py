"""Static contract checks only: these do not execute ChatGPT or prove behavior."""
import hashlib
from pathlib import Path
import re
import sys
import subprocess
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_distribution import MODULES, PACKAGE, render  # noqa: E402


class DistributionTests(unittest.TestCase):
    def setUp(self):
        self.standalone = (ROOT / "SKINCARE_ASSISTANT_CHATGPT.md").read_text(encoding="utf-8")
        self.onboarding = (ROOT / "references/onboarding.md").read_text(encoding="utf-8")

    def test_generated_output_matches_sources(self):
        self.assertEqual(self.standalone, render())
        self.assertIn("v2.8.1 Draft 9", self.standalone.splitlines()[0])
        self.assertEqual(PACKAGE, "skincare-assistant-v2.8.1-draft9.zip")
        for name in ("README.md", "INSTALL.md", "RELEASE_NOTES.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertIn("v2.8.1-draft9/SKINCARE_ASSISTANT_CHATGPT.md", text)
            self.assertNotIn("v2.8.1-draft8/SKINCARE_ASSISTANT_CHATGPT.md", text)

    def test_checksum_matches_current_file(self):
        digest = hashlib.sha256(self.standalone.encode()).hexdigest()
        self.assertEqual((ROOT / "SHA256SUMS.txt").read_text(), f"{digest}  SKINCARE_ASSISTANT_CHATGPT.md\n")

    def test_standalone_module_links_resolve(self):
        anchors = re.findall(r'<a id="([^"]+)"></a>', self.standalone)
        self.assertEqual(anchors, [f"module-{name}" for name in MODULES])
        for link in re.findall(r"\]\(#([^)]*)\)", self.standalone):
            self.assertIn(link, anchors)
        self.assertNotRegex(self.standalone, r"\]\((?:references/)?[a-z-]+\.md\)")

    def test_one_polished_welcome(self):
        for text in (self.onboarding, self.standalone):
            self.assertEqual(text.count("欢迎使用「护肤助理」。"), 1)
            self.assertEqual(text.count("尽量减少营销宣传对选择的干扰"), 1)
            self.assertIn("逐步调整长期护肤方案", text)
            self.assertNotIn("逐步建立属于你的护肤档案", text)

    def test_allergy_intake_and_submission_contracts(self):
        for phrase in ("开场过敏题只收集和记录已有信息", "同一轮直接提出下一道未回答的标准问题",
                       "不算请求", "同轮接回保存的待完成节点", "不强行回接",
                       "提交文本与摘要只表达用户实际回答", "长期保存仍需遵守"):
            self.assertIn(phrase, self.onboarding)

    def test_required_main_flow_gates_remain(self):
        for phrase in ("Q1 洁面后约30分钟", "Q2 刺激倾向", "Q3 最想改善的最多3项",
                       "逐张判断", "这份评估符合实际情况吗", "报告确认后询问常驻国家/地区",
                       "产品推荐怎么处理", "用户不愿提供照片时"):
            self.assertIn(phrase, self.onboarding)

    def test_trigger_boundary_replaces_ambiguous_followup(self):
        concerns = (ROOT / "references/concerns.md").read_text(encoding="utf-8")
        self.assertIn("这些是候选问题，不是必答清单", concerns)
        self.assertIn("提到历史反应不自动触发本条的调查或检索", concerns)
        self.assertNotIn("按需问：是否正在发作；新产品/药物", concerns)

    def test_product_and_return_state_contracts(self):
        products = (ROOT / "references/products.md").read_text(encoding="utf-8")
        storage = (ROOT / "references/storage.md").read_text(encoding="utf-8")
        self.assertIn("到产品匹配时应用开场记录", products)
        self.assertIn("不把其中所有成分一概判为过敏原", products)
        self.assertIn("待返回节点、已答标准题", storage)
        self.assertIn("报告确认/地区/产品模式的完成状态", storage)

    def test_medical_safety_not_displaced(self):
        safety = (ROOT / "references/safety.md").read_text(encoding="utf-8")
        for phrase in ("呼吸困难", "舌/喉肿胀", "立即联系当地急救", "STOP_ESCALATE", "不能把未知记为无症状"):
            self.assertIn(phrase, safety)
        self.assertIn("不用 Q1 分散急症处理", self.onboarding)
        self.assertIn("插问中出现新红旗仍以安全处理优先", self.onboarding)

    def test_behavior_cases_are_explicitly_unrun(self):
        cases = (ROOT / "tests/onboarding_regressions.md").read_text(encoding="utf-8")
        for number in range(1, 28):
            self.assertIn(f"R{number:02}", cases)
        self.assertIn("尚未运行真实 ChatGPT 行为测试", cases)

    def test_three_product_modes_and_legacy_semantics(self):
        for phrase in ("①告诉我正在用的具体产品", "②只告诉我喜欢的品牌", "③不提供产品或品牌",
                       "不增加第四选项", "原始语义", "不记为“没有产品”", "已有产品评估与用法"):
            self.assertIn(phrase, self.onboarding)
        self.assertNotIn("④品牌偏好和已有产品都有", self.onboarding)
        for phrase in ("owned_products", "brand_preference", "new_recommendation", "product_modes_v2", "旧档案只有裸数字"):
            self.assertIn(phrase, self.onboarding)

    def test_owned_product_output_and_problem_traceability(self):
        products = (ROOT / "references/products.md").read_text(encoding="utf-8")
        visuals = (ROOT / "references/visuals.md").read_text(encoding="utf-8")
        for text in (products, visuals):
            for phrase in ("已有产品评估与用法", "继续用／调整用法／暂停使用／信息不足", "问题编号"):
                self.assertIn(phrase, text)
        self.assertIn("不把品牌当已拥有的产品", self.onboarding)
        self.assertIn("先完成已知项和其他步骤", products)

    def test_eye_step_is_conditional_and_actionable(self):
        products = (ROOT / "references/products.md").read_text(encoding="utf-8")
        for phrase in ("无活动炎症/红旗", "眼霜／眼周护理步骤", "单次用量", "可涂部位",
                       "精华之后、面霜之前", "AM/PM与频次", "不自动加功效眼霜",
                       "不承诺眼霜消除结构性黑眼圈", "五步是默认基础，不是步骤数量上限"):
            self.assertIn(phrase, products)
        concerns = (ROOT / "references/concerns.md").read_text(encoding="utf-8")
        self.assertIn("## 13 眼周干燥", concerns)
        self.assertIn("眼痛、畏光或视力改变需及时医学评估", concerns)

    def test_package_integrity_and_reproducibility(self):
        command = [sys.executable, str(ROOT / "scripts/build_distribution.py"), "--check", "--package"]
        subprocess.run(command, check=True, capture_output=True)
        package = ROOT / "dist" / PACKAGE
        first = package.read_bytes()
        subprocess.run(command, check=True, capture_output=True)
        self.assertEqual(first, package.read_bytes())
        with zipfile.ZipFile(package) as archive:
            self.assertIsNone(archive.testzip())
            expected = {"SKILL.md", "SKINCARE_ASSISTANT_CHATGPT.md", "README.md", "INSTALL.md", "RELEASE_NOTES.md", "LICENSE-NONCOMMERCIAL.txt", "SHA256SUMS.txt"}
            expected.update(f"references/{name}.md" for name in MODULES)
            self.assertEqual(set(archive.namelist()), expected)
            for name in archive.namelist():
                self.assertEqual(archive.read(name), (ROOT / name).read_bytes())
        for line in (ROOT / "dist/SHA256SUMS.txt").read_text().splitlines():
            digest, name = line.split("  ", 1)
            self.assertEqual(digest, hashlib.sha256((ROOT / "dist" / name).read_bytes()).hexdigest())


if __name__ == "__main__":
    unittest.main()
