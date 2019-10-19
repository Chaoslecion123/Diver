from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

from . import VoteType


class Review(models.Model):
    product = models.ForeignKey(
        "product.Product",
        related_name='reviews',
        related_query_name='review',
        on_delete=models.CASCADE)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='reviews',
        related_query_name='review',
        on_delete=models.CASCADE)

    score = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    comment = models.TextField()

    created = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        unique_together = ('user', 'product')

    def get_upvotes_count(self):
        votes = getattr(self, 'votes', None)
        if votes:
            return votes.filter(type=VoteType.UP).count()
        return 0

    def get_downvotes_count(self):
        votes = getattr(self, 'votes', None)
        if votes:
            return votes.filter(type=VoteType.DOWN).count()
        return 0


class ReviewVote(models.Model):
    review = models.ForeignKey(
        Review,
        related_name='votes',
        related_query_name='vote',
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='review_votes',
        related_query_name='review_vote',
        on_delete=models.CASCADE
    )

    type = models.IntegerField(
        choices=VoteType.CHOICES,
        default=VoteType.UP
    )

    created = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        unique_together = ('user', 'review')
