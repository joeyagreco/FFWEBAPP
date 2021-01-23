import pandas as pd
import numpy as np

import plotly.graph_objects as go

from helpers.LeagueModelNavigator import LeagueModelNavigator
from models.league_models.LeagueModel import LeagueModel
from packages.StatCalculators.PpgCalculator import PpgCalculator


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
        # fig.show()
        html = fig.to_html(full_html=False, auto_play=False, include_plotlyjs=False)
        return html

    @staticmethod
    def getHtmlForScoringShare(leagueModel: LeagueModel):

        # TODO MAKE THIS INTO A LMN METHOD
        # get list of team names
        teamNames = []
        for team in leagueModel.getTeams():
            teamNames.append(team.getTeamName())

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

        # fig.show()
        html = fig.to_html(full_html=False, auto_play=False, include_plotlyjs=False)
        return html
