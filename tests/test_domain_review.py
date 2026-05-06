import unittest

from src.cobalt_tool_watch_mark.domain_review import DomainReview, review_lane, review_score


class DomainReviewTests(unittest.TestCase):
    def test_review_lane(self) -> None:
        item = DomainReview(45, 23, 32, 86)
        self.assertEqual(review_score(item), 103)
        self.assertEqual(review_lane(item), "hold")


if __name__ == "__main__":
    unittest.main()
