from django.apps import apps

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    AllowAny
)

from django_filters.rest_framework import DjangoFilterBackend
from rest_flex_fields import FlexFieldsModelViewSet

from ...serializers import ReviewSerializer
from ....reviews import VoteType


from ...permissions import ReadOnly


__all__ = [
    'ReviewViewSet',
]


Review = apps.get_model(*'reviews.Review'.split())
ReviewVote = apps.get_model(*'reviews.ReviewVote'.split())


class ReviewViewSet(FlexFieldsModelViewSet):
    """ViewSet for :model:`account.Review`

    `** Actions **`:

    create:
    Create a new `account.Review` instance.

    retrieve:
    Return the given `account.Review`.

    update:
    Update the given `account.Review`..

    delete:
    Delete the given `account.Review`, and return an empty response
    with HTTP 204 status code.

    list:
    Return a list of all the existing :model:`Review`.
    """

    permission_classes = [ReadOnly]
    lookup = 'id'
    permit_list_expands = ['user']

    queryset = Review.objects.order_by('created')
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter, ]
    filter_fields = [
        'user',
        'product',
    ]

    def get_permissions(self):
        permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]

    @action(
        methods=['post'],
        detail=True,
        name='upvote',
        url_path='upvote',
        url_name='upvote'
    )
    def upvote(self, request, *args, **kwargs):
        response_data = {
            'detail': 'Not authenticated user.',
            'code': 'not-authenticated'
        }
        response_status = status.HTTP_400_BAD_REQUEST

        review = self.get_object()
        user = self.request.user

        if user.is_authenticated:
            vote = ReviewVote.objects.filter(
                review=review,
                user=user
            ).first()

            if vote and vote.type == VoteType.UP:
                try:
                    vote.delete()
                    response_status = status.HTTP_200_OK
                    review = self.get_object()
                    response_data = ReviewSerializer(review, expand=["user"]).data
                except Exception as msg:  # pylint: disable=broad-except
                    response_data = {
                        'detail': str(msg),
                        'code': 'bad-operation'
                    }
            elif vote and vote.type == VoteType.DOWN:
                try:
                    vote.type = VoteType.UP
                    vote.save()
                    response_status = status.HTTP_200_OK
                    review = self.get_object()
                    response_data = ReviewSerializer(review, expand=["user"]).data
                except Exception as msg:  # pylint: disable=broad-except
                    response_data = {
                        'detail': str(msg),
                        'code': 'bad-operation'
                    }
            else:
                try:
                    vote = ReviewVote(
                        review=review,
                        user=user,
                        type=VoteType.UP
                    )
                    vote.save()
                    response_status = status.HTTP_201_CREATED
                    review = self.get_object()
                    response_data = ReviewSerializer(review, expand=["user"]).data
                except Exception as msg:  # pylint: disable=broad-except
                    response_data = {
                        'detail': str(msg),
                        'code': 'bad-operation'
                    }

        return Response(response_data, status=response_status)

    @action(
        methods=['post'],
        detail=True,
        name='downvote',
        url_path='downvote',
        url_name='downvote'
    )
    def downvote(self, request, *args, **kwargs):
        response_data = {
            'detail': 'Not authenticated user.',
            'code': 'not-authenticated'
        }
        response_status = status.HTTP_400_BAD_REQUEST

        review = self.get_object()
        user = self.request.user

        if user.is_authenticated:
            vote = ReviewVote.objects.filter(
                review=review,
                user=user
            ).first()

            if vote and vote.type == VoteType.DOWN:
                try:
                    vote.delete()
                    response_status = status.HTTP_200_OK
                    review = self.get_object()
                    response_data = ReviewSerializer(review, expand=["user"]).data
                except Exception as msg:  # pylint: disable=broad-except
                    response_data = {
                        'detail': str(msg),
                        'code': 'bad-operation'
                    }
            elif vote and vote.type == VoteType.UP:
                try:
                    vote.type = VoteType.DOWN
                    vote.save()
                    response_status = status.HTTP_200_OK
                    review = self.get_object()
                    response_data = ReviewSerializer(review, expand=["user"]).data
                except Exception as msg:  # pylint: disable=broad-except
                    response_data = {
                        'detail': str(msg),
                        'code': 'bad-operation'
                    }
            else:
                try:
                    vote = ReviewVote(
                        review=review,
                        user=user,
                        type=VoteType.DOWN
                    )
                    vote.save()
                    response_status = status.HTTP_201_CREATED
                    review = self.get_object()
                    response_data = ReviewSerializer(review, expand=["user"]).data
                except Exception as msg:  # pylint: disable=broad-except
                    response_data = {
                        'detail': str(msg),
                        'code': 'bad-operation'
                    }

        return Response(response_data, status=response_status)
