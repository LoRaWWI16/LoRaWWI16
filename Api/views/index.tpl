<!DOCTYPE html>
<html lang="de">
    <head>
        <title>Tablettenautomat</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <link type="text/css" rel="stylesheet" href="{{get_url('static', filename ='css/stylesheet.css')}}">
        <style>
            /* Set gray background color and 100% height */
            /* Remove the navbar's default margin-bottom and rounded borders */
            body {
                background-color: whitesmoke;
            }
            .rundrum {
                background-color:    white;
                border-width:        1px;
                border-style:        solid;
                border-color:        #e3e3e3;
                padding: 2em;
            }
            .well {
                background-color: white;
            }
            * {
                border-radius: 0 !important;
            }
            article {
                margin-top: 3em;
                margin-left: 3em;
                margin-right: 3em;
            }
            .navbar {
                margin-bottom: 0;
                border-radius: 0;
            }
            .navbar-inverse {
                background-color: #2a3f54;
            }
            .navbar-inverse .navbar-nav > .active > a {
                background-color: #2a3f54;
            }
            h1 {
                font-size: x-large;
                color: white;
                margin-left: 1em;
            }
            h2 {
                color: #2a3f54;
                font-size: x-large;
            }
            h4 {
                font-size: xx-large;
                color: #24bb9c;
                text-align: center;
                font-weight: bolder;
            }
            h3 {
                font-size: medium;
                font-weight: bold;
                color: #2a3f54;
                text-align: center;
              }
            .chart {
                width: 100%;
            }
            #1 {
                background-color: lightyellow !important;
                border-color: yellow;
            }
        </style>
    </head>
    <body>
        <header>
            <nav class="navbar navbar-inverse">
                <div class="container-fluid">
                    <h1>Dashboard Tablettenautomat</h1>
                </div>
            </nav>
        </header>
        <article>
            <div class="row">
                <div class="col-md-4">
                    % if dur > 28800:
                        % if days >= 1:
                        <div class="well" style="background-color: lightpink">
                            <h3>Letzte Verbindung zum TTN vor</h3>
                            <hr style="border-color: lightcoral">
                            <h4 style="color: lightcoral">{{days}}d</h4>
                        </div>
                        % else:
                        <div class="well" style="background-color: lightyellow">
                            <h3 >Letzte Verbindung zum TTN vor</h3>
                            <hr style="border-color: darkgoldenrod">
                            <h4 style="color: darkgoldenrod">{{hours}}h</h4>
                        </div>
                        % end
                    % else:
                        <div class="well">
                            <h3>Letzte Verbindung zum TTN vor</h3>
                            <hr>
                            <h4>
                                {{hours}}h
                            </h4>
                        </div>
                    % end
                </div>
                <div class="col-md-4">
                    <div class="well">
                        <h3>Anzahl empfangene Daten</h3>
                        <hr>
                        <h4>{{count}}</h4>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="well">
                        <h3>Erste Verbindung</h3>
                        <hr>
                        <h4>{{first[0].strftime("%d")}} {{first[0].strftime("%b")}} {{first[0].strftime("%y")}}</h4>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-md-8">
                    <div class="well">
                        <h2>Anzahl Empfangene Daten pro Tag</h2>
                        <hr>
                        <img src=" {{get_url('static', filename ='histo.png')}}" alt="Histogramm" class="chart">
                    </div>
                    <div class="rundrum">
                        <h2>Alle empfangenen Daten</h2>
                        <hr>
                        <table class="table">
                            <thead>
                                <tr>
                                    <th>
                                        Zeitpunkt
                                    </th>
                                    <th>
                                        Daten
                                    </th>
                                </tr>
                            </thead>
                            <tbody>
                            %for i in row:
                                <tr>
                                    <td>{{i[0]}}</td>
                                    <td>{{i[1]}}</td>
                                </tr>
                            %end
                            </tbody>
                        </table>
                    </div>
                </div>
                <div class="col-md-4">
                    % if durdate<86400:
                    <div class="well">
                        <h3>Letzte Tablettenausgabe vor</h3>
                        <hr>
                        <h4>{{dutydateh}}h</h4>
                    </div>
                    % else:
                    <div class="well" style="background-color: lightpink">
                        <h3>Letzte Tablettenausgabe vor</h3>
                        <hr style="border-color: lightcoral">
                        <h4 style="color: lightcoral">{{dutydateh}}h</h4>
                    </div>
                    % end
                    % if durupdate<604800:
                    <div class="well">
                        <h3>Letzte Tablettenbestückung vor</h3>
                        <hr>
                        <h4>{{fillupdateh}}h</h4>
                    </div>
                    % else:
                    <div class="well" style="background-color: lightpink">
                        <h3>Letzte Tablettenbestückung vor</h3>
                        <hr style="border-color: lightcoral">
                        <h4 style="color: lightcoral">{{fillupdateh/24}}d</h4>
                    </div>
                    % end
                    <div class="rundrum">
                        <h2>Empfangene Datentypen</h2>
                        <hr>
                        <img src=" {{get_url('static', filename ='donut.png')}}" alt="Kuchendiagramm" class="chart">
                    </div>
                </div>
            </div>
        </article>
    </body>
</html>