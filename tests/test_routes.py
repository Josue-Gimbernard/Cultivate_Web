import unittest

from app import create_app


class RouteTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config.update(TESTING=True, PREVIEW_ACCESS_CODE="")
        self.client = self.app.test_client()

    def test_healthz(self):
        response = self.client.get("/healthz")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["service"], "cultivate-web")

    def test_preview_routes(self):
        for route in [
            "/",
            "/owner-preview",
            "/review-command-center",
            "/owner-brief",
            "/next-actions",
            "/day-at-cultivate",
            "/spaces",
            "/brand-voice",
            "/membership-model",
            "/family-journey",
            "/launch-roadmap",
            "/faq-lab",
            "/source-evidence",
            "/why-cultivate",
            "/glossary",
            "/what-cultivate-is",
            "/assumptions-review",
            "/public-draft-hub",
            "/draft-home",
            "/draft-about",
            "/draft-cohort",
            "/draft-faq",
            "/approval-matrix",
            "/founding-family-interest",
            "/owner-decisions",
            "/owner-walkthrough",
            "/ecosystem-map",
            "/founding-cohort",
            "/cohort-blueprint",
            "/impact-signals",
            "/launch-readiness",
            "/owner-input-packet",
            "/owner-review-worksheet",
            "/owner-answer-log",
            "/post-meeting-update-plan",
            "/owner-review-prep",
            "/ui-kitchen-sink",
            "/ux-lab",
        ]:
            with self.subTest(route=route):
                response = self.client.get(route)
                self.assertEqual(response.status_code, 200)
                self.assertIn(b"Cultivate", response.data)

    def test_new_preview_pages_include_core_content(self):
        expectations = {
            "/day-at-cultivate": b"A day at Cultivate",
            "/review-command-center": b"Run the owner review",
            "/owner-brief": b"The short version",
            "/next-actions": b"Turn the preview",
            "/spaces": b"The campus, piece by piece.",
            "/brand-voice": b"Brand Voice Lab",
            "/membership-model": b"How the ecosystem could earn.",
            "/family-journey": b"From curiosity to belonging.",
            "/launch-roadmap": b"Sequence the work",
            "/faq-lab": b"Answer the hard questions",
            "/source-evidence": b"Show where the website",
            "/why-cultivate": b"A careful answer to the family need",
            "/glossary": b"Shared language",
            "/what-cultivate-is": b"Explain the category",
            "/assumptions-review": b"Name what we are treating as true",
            "/public-draft-hub": b"Prepare the public site",
            "/draft-home": b"Draft public homepage",
            "/draft-about": b"Draft public About",
            "/draft-cohort": b"Draft public Founding Cohort",
            "/draft-faq": b"Draft public FAQ",
            "/approval-matrix": b"Separate ready claims",
            "/founding-family-interest": b"Help shape Cultivate",
            "/owner-decisions": b"The next decisions are shape decisions.",
            "/owner-walkthrough": b"A guided private presentation",
            "/ecosystem-map": b"Every space strengthens the village",
            "/founding-cohort": b"Founding Cohort Term",
            "/cohort-blueprint": b"Make the first term feel buildable.",
            "/impact-signals": b"Decide what to measure",
            "/launch-readiness": b"Show the vision. Protect the promises.",
            "/owner-input-packet": b"Collect the answers",
            "/owner-review-worksheet": b"Capture owner answers",
            "/owner-answer-log": b"Track what has actually been approved",
            "/post-meeting-update-plan": b"Turn owner answers into site changes",
            "/owner-review-prep": b"Get the preview ready",
        }
        for route, text in expectations.items():
            with self.subTest(route=route):
                response = self.client.get(route)
                self.assertIn(text, response.data)

    def test_review_command_center_includes_curated_navigation(self):
        response = self.client.get("/review-command-center")
        for text in [
            b"Meeting modes",
            b"15 minute review",
            b"Public page prep",
            b"All rooms",
            b"Offer Model",
        ]:
            with self.subTest(text=text):
                self.assertIn(text, response.data)

    def test_guided_review_path_appears_on_primary_review_pages(self):
        expectations = {
            "/owner-preview": b"Continue to Command",
            "/review-command-center": b"Continue to Walkthrough",
            "/owner-walkthrough": b"Continue to Brief",
            "/owner-brief": b"Continue to Approvals",
            "/approval-matrix": b"Continue to Actions",
            "/next-actions": b"Move to public drafts",
        }
        for route, text in expectations.items():
            with self.subTest(route=route):
                response = self.client.get(route)
                self.assertIn(b"Guided owner review", response.data)
                self.assertIn(text, response.data)

    def test_public_draft_packet_navigation(self):
        expectations = {
            "/public-draft-hub": b"Draft set: Hub",
            "/draft-home": b"Draft set: Home",
            "/draft-about": b"Draft set: About",
            "/draft-cohort": b"Draft set: Cohort",
            "/draft-faq": b"Draft set: FAQ",
            "/founding-family-interest": b"Draft set: Interest",
        }
        for route, text in expectations.items():
            with self.subTest(route=route):
                response = self.client.get(route)
                self.assertIn(b"Private public-site packet", response.data)
                self.assertIn(text, response.data)

    def test_public_draft_pages_include_publishing_gate(self):
        for route in [
            "/public-draft-hub",
            "/draft-home",
            "/draft-about",
            "/draft-cohort",
            "/draft-faq",
            "/founding-family-interest",
        ]:
            with self.subTest(route=route):
                response = self.client.get(route)
                self.assertIn(b"Publishing gate", response.data)
                self.assertIn(b"Category language", response.data)
                self.assertIn(b"Claim boundaries", response.data)
                self.assertIn(b"Intake and privacy", response.data)

    def test_approval_matrix_includes_status_snapshot(self):
        response = self.client.get("/approval-matrix")
        for text in [
            b"Approval snapshot",
            b"Ready for owner review",
            b"Needs confirmation",
            b"Validate first",
            b"Internal only",
            b"Blocked for public",
        ]:
            with self.subTest(text=text):
                self.assertIn(text, response.data)

    def test_next_actions_includes_lane_snapshot(self):
        response = self.client.get("/next-actions")
        for text in [
            b"Action lanes",
            b"Owner approval queue",
            b"Validation queue",
            b"Web build queue",
            b"Evidence queue",
        ]:
            with self.subTest(text=text):
                self.assertIn(text, response.data)

    def test_owner_decisions_include_risk_snapshot(self):
        response = self.client.get("/owner-decisions")
        for text in [
            b"Decision agenda",
            b"Low risk",
            b"Medium risk",
            b"High risk",
            b"safe first lane",
        ]:
            with self.subTest(text=text):
                self.assertIn(text, response.data)

    def test_safe_without_owner_support_pages(self):
        expectations = {
            "/why-cultivate": [
                b"Need, response, boundary",
                b"Do not promise coworking availability",
                b"Do not advertise childcare",
            ],
            "/glossary": [
                b"Founding cohort",
                b"The Summit",
                b"Do not publish as available childcare",
            ],
            "/what-cultivate-is": [
                b"Is not",
                b"A licensed school, daycare",
                b"full-campus availability",
            ],
            "/assumptions-review": [
                b"Assumptions are not approvals",
                b"Owner must approve final public category wording",
                b"Owner must approve publishing gate items",
            ],
        }
        for route, texts in expectations.items():
            response = self.client.get(route)
            for text in texts:
                with self.subTest(route=route, text=text):
                    self.assertIn(text, response.data)

    def test_owner_input_packet_names_owner_dependent_work(self):
        response = self.client.get("/owner-input-packet")
        for text in [
            b"founder origin story",
            b"What should Cultivate call itself",
            b"Who is the first cohort actually for",
            b"What information can an interest form collect",
            b"public guesses",
            b"Approval Matrix",
        ]:
            with self.subTest(text=text):
                self.assertIn(text, response.data)

    def test_owner_review_worksheet_is_meeting_ready(self):
        response = self.client.get("/owner-review-worksheet")
        for text in [
            b"Print worksheet",
            b"Owner answer",
            b"Approved",
            b"Validate",
            b"founder origin story",
            b"Update approvals before public drafts",
        ]:
            with self.subTest(text=text):
                self.assertIn(text, response.data)

    def test_owner_answer_log_starts_pending(self):
        response = self.client.get("/owner-answer-log")
        for text in [
            b"Pending owner answers",
            b"Pending owner answer",
            b"Not approved for public use",
            b"memory/08-owner-answer-log.md",
            b"Update approval matrix",
        ]:
            with self.subTest(text=text):
                self.assertIn(text, response.data)

    def test_post_meeting_update_plan_orders_changes(self):
        response = self.client.get("/post-meeting-update-plan")
        for text in [
            b"Log before launch language",
            b"memory/08-owner-answer-log.md",
            b"APPROVAL_ITEMS in app.py",
            b"ASSUMPTION_ITEMS in app.py",
            b"Do not update public drafts from memory",
            b"Run tests and document the change",
        ]:
            with self.subTest(text=text):
                self.assertIn(text, response.data)

    def test_owner_review_prep_sets_meeting_readiness(self):
        response = self.client.get("/owner-review-prep")
        for text in [
            b"Prepare, present, capture, then update",
            b"Confirm the owner can reach the gated site",
            b"pricing, dates, childcare, cafe, Foxtail",
            b"Close with the answer log and update plan",
            b"Command Center",
            b"Update Plan",
        ]:
            with self.subTest(text=text):
                self.assertIn(text, response.data)

    def test_public_draft_hub_cards_link_to_drafts(self):
        response = self.client.get("/public-draft-hub")
        for text in [
            b"Open Home draft",
            b"Open About draft",
            b"Open Founding Cohort draft",
            b"Open FAQ draft",
            b"Open Interest draft",
        ]:
            with self.subTest(text=text):
                self.assertIn(text, response.data)

    def test_preview_gate_blocks_without_access(self):
        gated = create_app()
        gated.config.update(TESTING=True, PREVIEW_ACCESS_CODE="secret")
        client = gated.test_client()
        response = client.get("/")
        self.assertEqual(response.status_code, 401)


if __name__ == "__main__":
    unittest.main()
