<!DOCTYPE html>
<html lang="de">
    <head>
        <title>Tablettenautomat</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <link type="text/css" rel="stylesheet" href="static/css/style.css">
        <link href="static/img/chart.png">
    </head>
    <nav class="navbar navbar-inverse">
        <div class="container-fluid">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">Logo</a>
            </div>
            <div class="collapse navbar-collapse" id="myNavbar">
                <ul class="nav navbar-nav">
                    <li class="active"><a href="#">Dashboard</a></li>
                    <li><a href="#">Filter 1</a></li>
                    <li><a href="#">Filter 2</a></li>
                    <li><a href="#">Filter 3</a></li>
                </ul>
            </div>
        </div>
    </nav>
    <body>
        <h1>Datenübersicht Tablettenautomat</h1>
        <div class="container">
            <div class="col-sm-4">
                % if dur > 28800:
                    % if days > 1:
                    <div class="alert alert-danger" role="alert">
                        <h3 class="alert-heading">Letzte Verbindung zum TTN</h3>
                        <h4>vor {{days}} Tagen</h4>
                    </div>
                % elif days ==1:
                    <div class="alert alert-danger" role="alert">
                        <h3 class="alert-heading">Letzte Verbindung zum TTN</h3>
                        <h4>vor {{days}} Tag</h4>
                    </div>
                % else:
                    <div class="alert alert-warning" role="alert">
                        <h3 class="alert-heading">Letzte Verbindung zum TTN</h3>
                        <h4>vor {{hours}} Stunden</h4>
                    </div>
                % end
            </div>
            <div class="col-sm-4">
                <div class="well">
                    <h3>Anzahl empfangene Daten</h3>
                    <h4>{{count}}</h4>
                </div>
            </div>
            <div class="col-sm-4">
                <div class="well">
                    <h3>Erste Verbindung</h3>
                    <h4>{{first[0]}}</h4>
                </div>
            </div>
        </div>
        <div class="container">
            <div class="col-sm-8">
                <h2>Empfangene Daten</h2>
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
            <div class="col-sm-4">
                <h2>Kuchendiagramm</h2>
                <img src="" alt="Kuchendiagramm">
            </div>
        </div>
    </body>
</html>
