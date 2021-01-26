import pandas as pd
import numpy as np

import plotly.graph_objects as go

from helpers.LeagueModelNavigator import LeagueModelNavigator
from models.league_models.LeagueModel import LeagueModel
from packages.StatCalculators.AwalCalculator import AwalCalculator
from packages.StatCalculators.PpgCalculator import PpgCalculator
from packages.StatCalculators.RecordCalculator import RecordCalculator


class GraphBuilder:
    """
    This class is used to create graphs.
    """

    @staticmethod
    def getHtmlForPpg(leagueModel: LeagueModel):

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

        html = fig.to_html(full_html=False, auto_play=False, include_plotlyjs=False)
        return html

    @staticmethod
    def getHtmlForScoringShare(leagueModel: LeagueModel):

        # TODO make this into a LMN method
        # get list of team names
        teamNames = []
        for team in leagueModel.getTeams():
            teamNames.append(team.getTeamName())

        # TODO use total points instead of PPG
        ppgByTeam = []
        for team in leagueModel.getTeams():
            ppgCalculator = PpgCalculator(team.getTeamId(), leagueModel)
            ppgByTeam.append(ppgCalculator.getPpg())

        trace = go.Pie(labels=teamNames, values=ppgByTeam)

        data = [trace]

        fig = go.Figure(data=data)

        fig.update_layout(
            title="Scoring Share"
        )

        html = fig.to_html(full_html=False, auto_play=False, include_plotlyjs=False)
        return html

    @staticmethod
    def getHtmlForAwalOverPpg(leagueModel: LeagueModel):

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

        html = fig.to_html(full_html=False, auto_play=False, include_plotlyjs=False)
        return html

    @staticmethod
    def getHtmlForAllScores(leagueModel: LeagueModel):

        allScores = []
        for team in leagueModel.getTeams():
            allScores += LeagueModelNavigator.getListOfTeamScores(leagueModel, team.getTeamId())

        data = np.array(allScores)
        data = [go.Histogram(x=data,
                             nbinsx=int(len(allScores)/2))]

        fig = go.Figure(data)

        fig.update_layout(
            xaxis=dict(title="Points Scored"),
            yaxis=dict(title="Occurrences"),
            title="Frequency of Scores"
        )

        html = fig.to_html(full_html=False, auto_play=False, include_plotlyjs=False)
        return html

    @staticmethod
    def getHtmlForPointsOverPointsAgainst(leagueModel: LeagueModel, screenWidth: int):
        data = dict()
        for team in leagueModel.getTeams():
            data[team.getTeamId()] = LeagueModelNavigator.getListOfTeamScores(leagueModel, team.getTeamId(), andOpponentScore=True)

        fig = go.Figure()

        for teamId in data.keys():
            fig.add_trace(go.Scatter(x=[matchup[0] for matchup in data[teamId]],
                                     y=[matchup[1] for matchup in data[teamId]],
                                     name=LeagueModelNavigator.getTeamById(leagueModel, teamId).getTeamName(),
                                     mode="markers",
                                     marker=dict(size=10)
                                     )
                          )

        # draw average line [linear regression]
        # pointsForList = []
        # pointsAgainstList = []
        # for teamId in data.keys():
        #     for matchup in data[teamId]:
        #         pointsForList.append(matchup[0])
        #         pointsAgainstList.append(matchup[1])
        # m, b = np.polyfit(np.array(pointsForList), np.array(pointsAgainstList), 1)
        # fig.add_trace(go.Scatter(x=pointsForList,
        #                          y=m * np.array(pointsAgainstList) + b,
        #                          showlegend=False,
        #                          mode="lines",
        #                          marker=dict(color="rgba(0,0,0,0.25)")
        #                          )
        #               )

        # TODO fix how screen width is used in this class
        if screenWidth:
            width = int(screenWidth)/2
        else:
            print("no width gotten")
            width = 960
        height = 0.8 * width
        fig.update_layout(
            xaxis=dict(title="Points For"),
            yaxis=dict(title="Points Against"),
            title="Points For / Points Against",
            width=width,
            height=height
        )

        html = fig.to_html(full_html=False, auto_play=False, include_plotlyjs=False)
        return html
