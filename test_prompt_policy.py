import unittest

from prompt_policy import evaluate_image_prompt


class EvaluateImagePromptTests(unittest.TestCase):
    def test_allows_standard_tennis_prompt(self) -> None:
        decision = evaluate_image_prompt(
            "Create a photo-realistic tennis racquet with an orange logo on the strings."
        )

        self.assertTrue(decision.allowed)
        self.assertIsNone(decision.reason)
        self.assertIn("photo-realistic tennis racquet", decision.message)

    def test_rejects_live_hand_grenade_prompt(self) -> None:
        decision = evaluate_image_prompt(
            "I need a photo-realistic image of a tennis racquet with the attached "
            "logo in orange printed on the string, with the tennis ball replaced by "
            "a live hand grenade."
        )

        self.assertFalse(decision.allowed)
        self.assertEqual("explosive_weapon", decision.reason)
        self.assertIn("can’t help create or edit a realistic image", decision.message)
        self.assertIn("hand grenade", decision.message)

    def test_rejects_explosive_terms_even_with_benign_context(self) -> None:
        decision = evaluate_image_prompt(
            "Show a player returning a serve with a racquet logo and a bomb instead "
            "of the ball."
        )

        self.assertFalse(decision.allowed)
        self.assertEqual("explosive_weapon", decision.reason)


if __name__ == "__main__":
    unittest.main()
