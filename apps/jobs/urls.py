from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'challenge/(?P<challenge_id>[0-9]+)/'
        r'challenge_phase/(?P<challenge_phase_id>[0-9]+)/submission/(?P<submission_id>[0-9]+)',
        views.change_submission_visibility, name='change_submission_visibility'),
    url(r'challenge/(?P<challenge_id>[0-9]+)/'
        r'challenge_phase/(?P<challenge_phase_id>[0-9]+)/submission/',
        views.challenge_submission, name='challenge_submission'),
    url(r'challenge_phase_split/(?P<challenge_phase_split_id>[0-9]+)/leaderboard/',
        views.leaderboard, name='leaderboard'),
]
