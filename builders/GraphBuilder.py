import pandas as pd
import numpy as np

import plotly.graph_objects as go

from helpers.LeagueModelNavigator import LeagueModelNavigator
from models.league_models.LeagueModel import LeagueModel


class GraphBuilder:
    """
    This class is used to create graphs.
    """

    @staticmethod
    def getHtmlForPpg(leagueModel: LeagueModel):

        data = dict()
        for team in leagueModel.getTeams():
            data[team.getTeamId()] = []
        for week in leagueModel.getWeeks():
            for matchup in week.getMatchups():
                data[matchup.getTeamA().getTeamId()].append(matchup.getTeamAScore())
                data[matchup.getTeamB().getTeamId()].append(matchup.getTeamBScore())

        # df_scores = pd.DataFrame(data=data)
        print(data)
        xAxisTicks = list(range(1, len(data[list(data.keys())[0]]) + 1))

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
        html = fig.to_html(full_html=True, auto_play=False, include_plotlyjs=True)
        return html


