import pandas as pd
import numpy as np

import plotly.graph_objects as go
from plotly.graph_objs import Figure

from helpers.LeagueModelNavigator import LeagueModelNavigator
from models.league_models.LeagueModel import LeagueModel
from packages.StatCalculators.AwalCalculator import AwalCalculator
from packages.StatCalculators.PpgCalculator import PpgCalculator
from packages.StatCalculators.RecordCalculator import RecordCalculator


class GraphBuilder:
    """
    This class is used to create graphs.
    """
    DEFAULT_WIDTH = 960
    WIDTH_MULTIPLIER = 0.5
    HEIGHT_MULTIPLIER = 0.8

    @classmethod
    def __setWidthOfFig(cls, fig: Figure, screenWidth: float):
        if screenWidth:
            width = int(screenWidth) * cls.WIDTH_MULTIPLIER
        else:
            width = cls.DEFAULT_WIDTH
        height = cls.HEIGHT_MULTIPLIER * width
        fig.update_layout(
            width=width,
            height=height
        )

    @classmethod
    def getHtmlForPpg(cls, leagueModel: LeagueModel, screenWidth: float):

        data = dict()
        for team in leagueModel.getTeams():
            data[team.getTeamId()] = LeagueModelNavigator.getListOfTeamScores(leagueModel, team.getTeamId())

        # df_scores = pd.DataFrame(data=data)
        xAxisTicks = LeagueModelNavigator.getNumberOfWeeksInLeague(leagueModel, asList=True)

        fig = go.Figure()

        for teamId in data.keys():
            fig.add_trace(go.Scatter(x=xAxisTicks,
                                     y=data[teamId],
                                     name=LeagueModelNavigator.getTeamById(leagueModel, teamId).getTeamName(),
                                     mode="lines+markers"))

        fig.update_layout(
            xaxis=dict(title="Week",
                       tickvals=xAxisTicks),
            yaxis=dict(title="Points Scored"),
            title="PPG by Week"
        )

        cls.__setWidthOfFig(fig, screenWidth)

        html = fig.to_html(full_html=False, auto_play=False, include_plotlyjs=False)
        return html

    @classmethod
    def getHtmlForScoringShare(cls, leagueModel: LeagueModel, screenWidth: float):

        teamNames = []
        ppgByTeam = []
        for team in leagueModel.getTeams():
            teamNames.append(team.getTeamName())
            totalPoints = LeagueModelNavigator.totalPointsScoredByTeam(leagueModel, team.getTeamId())
            ppgByTeam.append(totalPoints)

        trace = go.Pie(labels=teamNames, values=ppgByTeam)

        data = [trace]

        fig = go.Figure(data=data)

        fig.update_layout(
            title="Scoring Share"
        )

        cls.__setWidthOfFig(fig, screenWidth)

        html = fig.to_html(full_html=False, auto_play=False, include_plotlyjs=False)
        return html

    @classmethod
    def getHtmlForAwalOverPpg(cls, leagueModel: LeagueModel, screenWidth: float):

        data = dict()
        ppgList = []
        awalList = []
        for team in leagueModel.getTeams():
            recordCalculator = RecordCalculator(team.getTeamId(), leagueModel)
            ppgCalculator = PpgCalculator(team.getTeamId(), leagueModel)
            awalCalculator = AwalCalculator(team.getTeamId(), leagueModel, recordCalculator.getWins(),
                                            recordCalculator.getTies())
            ppg = ppgCalculator.getPpg()
            awal = awalCalculator.getAwal()
            ppgList.append(ppg)
            awalList.append(awal)
            data[team.getTeamId()] = ([awal], [ppg])

        fig = go.Figure()

        for teamId in data.keys():
            fig.add_trace(go.Scatter(x=data[teamId][0],
                                     y=data[teamId][1],
                                     name=LeagueModelNavigator.getTeamById(leagueModel, teamId).getTeamName(),
                                     mode="markers",
                                     marker=dict(size=20)
                                     )
                          )
        # draw average line [linear regression]
        m, b = np.polyfit(np.array(awalList), np.array(ppgList), 1)
        fig.add_trace(go.Scatter(x=awalList,
                                 y=m * np.array(awalList) + b,
                                 showlegend=False,
                                 mode="lines",
                                 marker=dict(color="rgba(0,0,0,0.25)")
                                 )
                      )

        fig.update_layout(
            xaxis=dict(title="AWAL", dtick=0.5),
            yaxis=dict(title="PPG"),
            title="AWAL/PPG by Team"
        )

        cls.__setWidthOfFig(fig, screenWidth)

        html = fig.to_html(full_html=False, auto_play=False, include_plotlyjs=False)
        return html

    @classmethod
    def getHtmlForFrequencyOfScores(cls, leagueModel: LeagueModel, screenWidth: float):

        allScores = []
        for team in leagueModel.getTeams():
            allScores += LeagueModelNavigator.getListOfTeamScores(leagueModel, team.getTeamId())

        data = np.array(allScores)
        data = [go.Histogram(x=data,
                             nbinsx=int(len(allScores) / 2))]

        fig = go.Figure(data)

        fig.update_layout(
            xaxis=dict(title="Points Scored"),
            yaxis=dict(title="Occurrences"),
            title="Frequency of Scores"
        )

        cls.__setWidthOfFig(fig, screenWidth)

        html = fig.to_html(full_html=False, auto_play=False, include_plotlyjs=False)
        return html

    @classmethod
    def getHtmlForPointsOverPointsAgainst(cls, leagueModel: LeagueModel, screenWidth: float):
        data = dict()
        for team in leagueModel.getTeams():
            data[team.getTeamId()] = LeagueModelNavigator.getListOfTeamScores(leagueModel, team.getTeamId(),
                                                                              andOpponentScore=True)

        fig = go.Figure()

        for teamId in data.keys():
            fig.add_trace(go.Scatter(x=[matchup[0] for matchup in data[teamId]],
                                     y=[matchup[1] for matchup in data[teamId]],
                                     name=LeagueModelNavigator.getTeamById(leagueModel, teamId).getTeamName(),
                                     mode="markers",
                                     marker=dict(size=10)
                                     )
                          )

        fig.update_layout(
            xaxis=dict(title="Points For"),
            yaxis=dict(title="Points Against"),
            title="Points For / Points Against"
        )

        cls.__setWidthOfFig(fig, screenWidth)

        html = fig.to_html(full_html=False, auto_play=False, include_plotlyjs=False)
        return html
