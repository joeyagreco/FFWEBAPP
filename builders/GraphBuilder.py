import pandas as pd
import numpy as np

import plotly.graph_objects as go
from plotly.graph_objs import Figure

from helpers.Constants import Constants
from helpers.LeagueModelNavigator import LeagueModelNavigator
from models.league_models.LeagueModel import LeagueModel
from packages.StatCalculators.AwalCalculator import AwalCalculator
from packages.StatCalculators.PpgCalculator import PpgCalculator
from packages.StatCalculators.RecordCalculator import RecordCalculator
from packages.StatCalculators.StrengthOfScheduleCalculator import StrengthOfScheduleCalculator


class GraphBuilder:
    """
    This class is used to create graphs.
    """
    DEFAULT_WIDTH = 960
    WIDTH_MULTIPLIER = 0.5
    HEIGHT_MULTIPLIER = 0.8

    @classmethod
    def __setWidthAndHeightOfFig(cls, fig: Figure, screenWidth: float):
        """
        This sets the width and height of the given figure.
        """
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
    def getHtmlForByWeekLineGraph(cls, screenWidth: float, data: dict, xAxisTicks: list, yAxisName: str,
                                  yAxisDTick: float, title: str):
        """
        This turns the given data into a by week line graph.
        """
        fig = go.Figure()
        for teamName in data.keys():
            fig.add_trace(go.Scatter(x=xAxisTicks,
                                     y=data[teamName],
                                     name=teamName,
                                     mode="lines+markers"))
        fig.update_layout(
            xaxis=dict(title="Week",
                       tickvals=xAxisTicks),
            yaxis=dict(title=yAxisName, dtick=yAxisDTick),
            title=title
        )
        cls.__setWidthAndHeightOfFig(fig, screenWidth)
        return fig.to_html(full_html=False, auto_play=False, include_plotlyjs=False)

    @classmethod
    def getHtmlForPieGraph(cls, screenWidth: float, dataNames: list, dataValues: list, title: str) -> str:
        """
        This creates a pie graph for the given dataNames at the given dataValues.
        NOTE: dataNames should be in the same order as their corresponding dataValues.
        """
        trace = go.Pie(labels=dataNames, values=dataValues)
        data = [trace]
        fig = go.Figure(data=data)
        fig.update_layout(title=title)
        if not screenWidth:
            screenWidth = cls.DEFAULT_WIDTH
        fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=screenWidth / 100,
                          marker=dict(line=dict(color='#000000', width=2)))
        cls.__setWidthAndHeightOfFig(fig, screenWidth)
        return fig.to_html(full_html=False, auto_play=False, include_plotlyjs=False)

    @classmethod
    def getHtmlForHistogram(cls, screenWidth: float, data: list, bucketSize: int, xAxisName: str, yAxisName: str,
                            title: str) -> str:
        """
        This creates a histogram for the given data.
        """
        data = np.array(data)
        data = [go.Histogram(x=data, nbinsx=bucketSize)]
        fig = go.Figure(data)
        fig.update_layout(
            xaxis=dict(title=xAxisName),
            yaxis=dict(title=yAxisName),
            title=title
        )
        cls.__setWidthAndHeightOfFig(fig, screenWidth)
        return fig.to_html(full_html=False, auto_play=False, include_plotlyjs=False)

    @classmethod
    def getHtmlForAwalOverPpg(cls, leagueModel: LeagueModel, years: list, screenWidth: float) -> str:
        """
        This creates a scatter plot for AWAL/PPG for each team in the given leagueModel.
        """
        data = dict()
        ppgList = []
        awalList = []
        for year in years:
            for team in leagueModel.getYears()[year].getTeams():
                recordCalculator = RecordCalculator(team.getTeamId(), leagueModel, [year])
                ppgCalculator = PpgCalculator(team.getTeamId(), leagueModel, [year])
                awalCalculator = AwalCalculator(team.getTeamId(), leagueModel, [year], recordCalculator.getWins(), recordCalculator.getTies())
                ppg = ppgCalculator.getPpg()
                awal = awalCalculator.getAwal()
                ppgList.append(ppg)
                awalList.append(awal)
                data[f"{team.getTeamId()}-{year}"] = ([awal], [ppg])
        fig = go.Figure()
        for teamIdAndYear in data:
            teamId = int(teamIdAndYear[0:-5])
            year = teamIdAndYear[-4:]
            fig.add_trace(go.Scatter(x=data[teamIdAndYear][0],
                                     y=data[teamIdAndYear][1],
                                     name=LeagueModelNavigator.getTeamById(leagueModel, year, teamId).getTeamName(),
                                     mode="markers",
                                     marker=dict(size=20)
                                     )
                          )
        # draw average line [linear regression]
        m, b = np.polyfit(np.array(awalList), np.array(ppgList), 1)
        fig.add_trace(go.Scatter(x=awalList,
                                 y=m * np.array(awalList) + b,
                                 showlegend=False,
                                 name="Linear Regression",
                                 mode="lines",
                                 marker=dict(color="rgba(0,0,0,0.25)")
                                 )
                      )
        fig.update_layout(
            xaxis=dict(title="AWAL", dtick=0.5),
            yaxis=dict(title="PPG"),
            title=Constants.AWAL_OVER_PPG
        )
        cls.__setWidthAndHeightOfFig(fig, screenWidth)
        return fig.to_html(full_html=False, auto_play=False, include_plotlyjs=False)

    @classmethod
    def getHtmlForPointsOverPointsAgainst(cls, leagueModel: LeagueModel, years: list, screenWidth: float) -> str:
        """
        This creates a scatter plot for points scored/points against for every team in the given leagueModel.
        """
        data = dict()
        for year in years:
            for team in leagueModel.getYears()[year].getTeams():
                data[team.getTeamName()] = LeagueModelNavigator.getListOfTeamScores(leagueModel, year, team.getTeamId(), andOpponentScore=True)
        pointsForList = []
        pointsAgainstList = []
        fig = go.Figure()
        for teamName in data:
            teamPointsFor = [matchup[0] for matchup in data[teamName]]
            teamPointsAgainst = [matchup[1] for matchup in data[teamName]]
            pointsForList += teamPointsFor
            pointsAgainstList += teamPointsAgainst
            fig.add_trace(go.Scatter(x=teamPointsFor,
                                     y=teamPointsAgainst,
                                     name=teamName,
                                     mode="markers",
                                     marker=dict(size=10)
                                     )
                          )
        # draw average line [linear regression]
        m, b = np.polyfit(np.array(pointsForList), np.array(pointsAgainstList), 1)
        fig.add_trace(go.Scatter(x=pointsForList,
                                 y=m * np.array(pointsForList) + b,
                                 showlegend=False,
                                 name="Linear Regression",
                                 mode="lines",
                                 marker=dict(color="rgba(0,0,0,0.25)")
                                 )
                      )
        fig.update_layout(
            xaxis=dict(title="Points For"),
            yaxis=dict(title="Points Against"),
            title=Constants.POINTS_FOR_OVER_POINTS_AGAINST
        )
        cls.__setWidthAndHeightOfFig(fig, screenWidth)
        return fig.to_html(full_html=False, auto_play=False, include_plotlyjs=False)

    @classmethod
    def getHtmlForStrengthOfScheduleOverPPGAgainst(cls, leagueModel: LeagueModel, years: list, screenWidth: float) -> str:
        """
        This creates a scatter plot for points scored/points against for every team in the given leagueModel.
        """
        data = dict()
        sosList = []
        ppgAgainstList = []
        for year in years:
            for team in leagueModel.getYears()[year].getTeams():
                sosCalculator = StrengthOfScheduleCalculator(team.getTeamId(), leagueModel, [year])
                ppgCalculator = PpgCalculator(team.getTeamId(), leagueModel, [year])
                sos = sosCalculator.getStrengthOfSchedule()
                ppgAgainst = ppgCalculator.getPpgAgainst()
                sosList.append(sos)
                ppgAgainstList.append(ppgAgainst)
                data[team.getTeamName()] = ([sos], [ppgAgainst])
        fig = go.Figure()
        for teamName in data:
            fig.add_trace(go.Scatter(x=data[teamName][0],
                                     y=data[teamName][1],
                                     name=teamName,
                                     mode="markers",
                                     marker=dict(size=20)
                                     )
                          )
        # draw average line [linear regression]
        m, b = np.polyfit(np.array(sosList), np.array(ppgAgainstList), 1)
        fig.add_trace(go.Scatter(x=sosList,
                                 y=m * np.array(sosList) + b,
                                 showlegend=False,
                                 name="Linear Regression",
                                 mode="lines",
                                 marker=dict(color="rgba(0,0,0,0.25)")
                                 )
                      )

        fig.update_layout(
            xaxis=dict(title="Strength of Schedule", dtick=0.5),
            yaxis=dict(title="PPG Against"),
            title=Constants.STRENGTH_OF_SCHEDULE_OVER_PPG_AGAINST
        )
        cls.__setWidthAndHeightOfFig(fig, screenWidth)
        return fig.to_html(full_html=False, auto_play=False, include_plotlyjs=False)
