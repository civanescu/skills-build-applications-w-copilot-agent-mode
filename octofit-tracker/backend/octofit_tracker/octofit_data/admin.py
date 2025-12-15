from django.contrib import admin
from .models import Team, Activity, Workout, Leaderboard

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'reps')

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'score')
