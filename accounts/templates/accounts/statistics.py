<!doctype html>
<html lang="en">

<head>
    {% load static %}
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <title>Aarogya Setu|Statistics</title>
    <link rel="icon" href="https://upload.wikimedia.org/wikipedia/commons/4/41/Aarogya_Setu_App_Logo.png"
        type="image/x-icon">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link href="{% static 'open-iconic/font/css/open-iconic-bootstrap.css' %}" rel="stylesheet">
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link
        href="https://fonts.googleapis.com/css2?family=Encode+Sans+Semi+Condensed&family=Ubuntu+Condensed&display=swap"
        rel="stylesheet">
</head>
<style>
    body {
        font-family: 'Encode Sans Semi Condensed', sans-serif;
        font-family: 'Ubuntu Condensed', sans-serif;
        font-size: 20px;
    }

    #design {
        background-color: black;
        border: none;
        color: white;
        padding: 8px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 12px;
        font-family: 'Ubuntu', sans-serif;
    }

    .ad_footer_block {
        background-color: #005792;
    }

    .content1 {
        border-radius: 20px;
        padding: 10px 10px;
        margin: 10px auto;
        background-color: #ffdf6b;
        width: 100%;
    }

    .content1:hover {
        transition: background-color 0.5s ease;
        background-color:#ff8303;
    }
</style>

<body>
    <header>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="{% url 'home' %}">
                <img src="https://www.aarogyasetu.gov.in/wp-content/themes/setu/assets/images/aarogya_logo.png"
                    height=60 width=220 class="d-inline-block alighn-top" />
            </a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup"
                aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                <div class="navbar-nav ml-auto">
                    {% if user.is_authenticated %}
                    <a class="nav-item nav-link" href="">covid-19 STATISTICS</a>
                    <a class="nav-item nav-link" href="{% url 'vaccine' %}">VACCINATION</a>
                    <a class="nav-item nav-link" href="{% url 'covid' %}">covid-19 CHECKER</a>
                    <a class="nav-item nav-link" href="javascript:{document.getElementById('logout').submit()}"
                        onclick="">LOGOUT</a>
                    <form id="logout" method="POST" action="{% url 'logout' %}">
                        {% csrf_token %}
                        <input type="hidden" />
                    </form>
                    {% else %}
                    <a class="nav-item nav-link" href="{% url 'statistics' %}">covid-19 STATISTICS</a>
                    <a class="nav-item nav-link" href="{% url 'vaccine' %}">VACCINATION</a>
                    <a class="nav-item nav-link" href="{% url 'signup' %}">SIGN-UP/LOGIN</a>
                    {% endif %}
                </div>
        </nav>
    </header>
    <script>
        //https://api.covid19api.com/summary
        async function getcovidApi() {
            const jsonFormatData = await fetch('https://api.covid19india.org/data.json');
            const jsFormatData = await jsonFormatData.json();

            document.getElementById("a1").innerHTML = jsFormatData.statewise[0].confirmed;
            document.getElementById("a2").innerHTML = jsFormatData.statewise[0].recovered;
            document.getElementById("a3").innerHTML = jsFormatData.statewise[0].deaths;


            document.getElementById("b").innerHTML = jsFormatData.statewise[1].state;
            document.getElementById("b1").innerHTML = jsFormatData.statewise[1].confirmed;
            document.getElementById("b2").innerHTML = jsFormatData.statewise[1].recovered;
            document.getElementById("b3").innerHTML = jsFormatData.statewise[1].deaths;
            document.getElementById("b4").innerHTML = jsFormatData.statewise[1].lastupdatedtime;


            document.getElementById("c").innerHTML = jsFormatData.statewise[2].state;
            document.getElementById("c1").innerHTML = jsFormatData.statewise[2].confirmed;
            document.getElementById("c2").innerHTML = jsFormatData.statewise[2].recovered;
            document.getElementById("c3").innerHTML = jsFormatData.statewise[2].deaths;
            document.getElementById("c4").innerHTML = jsFormatData.statewise[2].lastupdatedtime;

            document.getElementById("d").innerHTML = jsFormatData.statewise[3].state;
            document.getElementById("d1").innerHTML = jsFormatData.statewise[3].confirmed;
            document.getElementById("d2").innerHTML = jsFormatData.statewise[3].recovered;
            document.getElementById("d3").innerHTML = jsFormatData.statewise[3].deaths;
            document.getElementById("d4").innerHTML = jsFormatData.statewise[3].lastupdatedtime;

            document.getElementById("e").innerHTML = jsFormatData.statewise[4].state;
            document.getElementById("e1").innerHTML = jsFormatData.statewise[4].confirmed;
            document.getElementById("e2").innerHTML = jsFormatData.statewise[4].recovered;
            document.getElementById("e3").innerHTML = jsFormatData.statewise[4].deaths;
            document.getElementById("e4").innerHTML = jsFormatData.statewise[4].lastupdatedtime;

            document.getElementById("f").innerHTML = jsFormatData.statewise[5].state;
            document.getElementById("f1").innerHTML = jsFormatData.statewise[5].confirmed;
            document.getElementById("f2").innerHTML = jsFormatData.statewise[5].recovered;
            document.getElementById("f3").innerHTML = jsFormatData.statewise[5].deaths;
            document.getElementById("f4").innerHTML = jsFormatData.statewise[5].lastupdatedtime;

            document.getElementById("g").innerHTML = jsFormatData.statewise[6].state;
            document.getElementById("g1").innerHTML = jsFormatData.statewise[6].confirmed;
            document.getElementById("g2").innerHTML = jsFormatData.statewise[6].recovered;
            document.getElementById("g3").innerHTML = jsFormatData.statewise[6].deaths;
            document.getElementById("g4").innerHTML = jsFormatData.statewise[6].lastupdatedtime;

            document.getElementById("h").innerHTML = jsFormatData.statewise[7].state;
            document.getElementById("h1").innerHTML = jsFormatData.statewise[7].confirmed;
            document.getElementById("h2").innerHTML = jsFormatData.statewise[7].recovered;
            document.getElementById("h3").innerHTML = jsFormatData.statewise[7].deaths;
            document.getElementById("h4").innerHTML = jsFormatData.statewise[7].lastupdatedtime;


            document.getElementById("i").innerHTML = jsFormatData.statewise[8].state;
            document.getElementById("i1").innerHTML = jsFormatData.statewise[8].confirmed;
            document.getElementById("i2").innerHTML = jsFormatData.statewise[8].recovered;
            document.getElementById("i3").innerHTML = jsFormatData.statewise[8].deaths;
            document.getElementById("i4").innerHTML = jsFormatData.statewise[8].lastupdatedtime;

            document.getElementById("j").innerHTML = jsFormatData.statewise[9].state;
            document.getElementById("j1").innerHTML = jsFormatData.statewise[9].confirmed;
            document.getElementById("j2").innerHTML = jsFormatData.statewise[9].recovered;
            document.getElementById("j3").innerHTML = jsFormatData.statewise[9].deaths;
            document.getElementById("j4").innerHTML = jsFormatData.statewise[9].lastupdatedtime;

            document.getElementById("k").innerHTML = jsFormatData.statewise[10].state;
            document.getElementById("k1").innerHTML = jsFormatData.statewise[10].confirmed;
            document.getElementById("k2").innerHTML = jsFormatData.statewise[10].recovered;
            document.getElementById("k3").innerHTML = jsFormatData.statewise[10].deaths;
            document.getElementById("k4").innerHTML = jsFormatData.statewise[10].lastupdatedtime;


            document.getElementById("l").innerHTML = jsFormatData.statewise[11].state;
            document.getElementById("l1").innerHTML = jsFormatData.statewise[11].confirmed;
            document.getElementById("l2").innerHTML = jsFormatData.statewise[11].recovered;
            document.getElementById("l3").innerHTML = jsFormatData.statewise[11].deaths;
            document.getElementById("l4").innerHTML = jsFormatData.statewise[11].lastupdatedtime;

            document.getElementById("m").innerHTML = jsFormatData.statewise[12].state;
            document.getElementById("m1").innerHTML = jsFormatData.statewise[12].confirmed;
            document.getElementById("m2").innerHTML = jsFormatData.statewise[12].recovered;
            document.getElementById("m3").innerHTML = jsFormatData.statewise[12].deaths;
            document.getElementById("m4").innerHTML = jsFormatData.statewise[12].lastupdatedtime;

            document.getElementById("n").innerHTML = jsFormatData.statewise[13].state;
            document.getElementById("n1").innerHTML = jsFormatData.statewise[13].confirmed;
            document.getElementById("n2").innerHTML = jsFormatData.statewise[13].recovered;
            document.getElementById("n3").innerHTML = jsFormatData.statewise[13].deaths;
            document.getElementById("n4").innerHTML = jsFormatData.statewise[13].lastupdatedtime;


            document.getElementById("o").innerHTML = jsFormatData.statewise[14].state;
            document.getElementById("o1").innerHTML = jsFormatData.statewise[14].confirmed;
            document.getElementById("o2").innerHTML = jsFormatData.statewise[14].recovered;
            document.getElementById("o3").innerHTML = jsFormatData.statewise[14].deaths;
            document.getElementById("o4").innerHTML = jsFormatData.statewise[14].lastupdatedtime;


            document.getElementById("p").innerHTML = jsFormatData.statewise[15].state;
            document.getElementById("p1").innerHTML = jsFormatData.statewise[15].confirmed;
            document.getElementById("p2").innerHTML = jsFormatData.statewise[15].recovered;
            document.getElementById("p3").innerHTML = jsFormatData.statewise[15].deaths;
            document.getElementById("p4").innerHTML = jsFormatData.statewise[15].lastupdatedtime;


            document.getElementById("q").innerHTML = jsFormatData.statewise[16].state;
            document.getElementById("q1").innerHTML = jsFormatData.statewise[16].confirmed;
            document.getElementById("q2").innerHTML = jsFormatData.statewise[16].recovered;
            document.getElementById("q3").innerHTML = jsFormatData.statewise[16].deaths;
            document.getElementById("q4").innerHTML = jsFormatData.statewise[16].lastupdatedtime;


            document.getElementById("r").innerHTML = jsFormatData.statewise[17].state;
            document.getElementById("r1").innerHTML = jsFormatData.statewise[17].confirmed;
            document.getElementById("r2").innerHTML = jsFormatData.statewise[17].recovered;
            document.getElementById("r3").innerHTML = jsFormatData.statewise[17].deaths;
            document.getElementById("r4").innerHTML = jsFormatData.statewise[17].lastupdatedtime;

            document.getElementById("s").innerHTML = jsFormatData.statewise[18].state;
            document.getElementById("s1").innerHTML = jsFormatData.statewise[18].confirmed;
            document.getElementById("s2").innerHTML = jsFormatData.statewise[18].recovered;
            document.getElementById("s3").innerHTML = jsFormatData.statewise[18].deaths;
            document.getElementById("s4").innerHTML = jsFormatData.statewise[18].lastupdatedtime;


            document.getElementById("t").innerHTML = jsFormatData.statewise[19].state;
            document.getElementById("t1").innerHTML = jsFormatData.statewise[19].confirmed;
            document.getElementById("t2").innerHTML = jsFormatData.statewise[19].recovered;
            document.getElementById("t3").innerHTML = jsFormatData.statewise[19].deaths;
            document.getElementById("t4").innerHTML = jsFormatData.statewise[19].lastupdatedtime;


            document.getElementById("u").innerHTML = jsFormatData.statewise[20].state;
            document.getElementById("u1").innerHTML = jsFormatData.statewise[20].confirmed;
            document.getElementById("u2").innerHTML = jsFormatData.statewise[20].recovered;
            document.getElementById("u3").innerHTML = jsFormatData.statewise[20].deaths;
            document.getElementById("u4").innerHTML = jsFormatData.statewise[20].lastupdatedtime;


            document.getElementById("v").innerHTML = jsFormatData.statewise[21].state;
            document.getElementById("v1").innerHTML = jsFormatData.statewise[21].confirmed;
            document.getElementById("v2").innerHTML = jsFormatData.statewise[21].recovered;
            document.getElementById("v3").innerHTML = jsFormatData.statewise[21].deaths;
            document.getElementById("v4").innerHTML = jsFormatData.statewise[21].lastupdatedtime;


            document.getElementById("w").innerHTML = jsFormatData.statewise[22].state;
            document.getElementById("w1").innerHTML = jsFormatData.statewise[22].confirmed;
            document.getElementById("w2").innerHTML = jsFormatData.statewise[22].recovered;
            document.getElementById("w3").innerHTML = jsFormatData.statewise[22].deaths;
            document.getElementById("w4").innerHTML = jsFormatData.statewise[22].lastupdatedtime;

            document.getElementById("x").innerHTML = jsFormatData.statewise[23].state;
            document.getElementById("x1").innerHTML = jsFormatData.statewise[23].confirmed;
            document.getElementById("x2").innerHTML = jsFormatData.statewise[23].recovered;
            document.getElementById("x3").innerHTML = jsFormatData.statewise[23].deaths;
            document.getElementById("x4").innerHTML = jsFormatData.statewise[23].lastupdatedtime;


            document.getElementById("y").innerHTML = jsFormatData.statewise[24].state;
            document.getElementById("y1").innerHTML = jsFormatData.statewise[24].confirmed;
            document.getElementById("y2").innerHTML = jsFormatData.statewise[24].recovered;
            document.getElementById("y3").innerHTML = jsFormatData.statewise[24].deaths;
            document.getElementById("y4").innerHTML = jsFormatData.statewise[24].lastupdatedtime;

            document.getElementById("z").innerHTML = jsFormatData.statewise[25].state;
            document.getElementById("z1").innerHTML = jsFormatData.statewise[25].confirmed;
            document.getElementById("z2").innerHTML = jsFormatData.statewise[25].recovered;
            document.getElementById("z3").innerHTML = jsFormatData.statewise[25].deaths;
            document.getElementById("z4").innerHTML = jsFormatData.statewise[25].lastupdatedtime;

            document.getElementById("aa").innerHTML = jsFormatData.statewise[26].state;
            document.getElementById("aa1").innerHTML = jsFormatData.statewise[26].confirmed;
            document.getElementById("aa2").innerHTML = jsFormatData.statewise[26].recovered;
            document.getElementById("aa3").innerHTML = jsFormatData.statewise[26].deaths;
            document.getElementById("aa4").innerHTML = jsFormatData.statewise[26].lastupdatedtime;


            document.getElementById("bb").innerHTML = jsFormatData.statewise[27].state;
            document.getElementById("bb1").innerHTML = jsFormatData.statewise[27].confirmed;
            document.getElementById("bb2").innerHTML = jsFormatData.statewise[27].recovered;
            document.getElementById("bb3").innerHTML = jsFormatData.statewise[27].deaths;
            document.getElementById("bb4").innerHTML = jsFormatData.statewise[27].lastupdatedtime;


            document.getElementById("cc").innerHTML = jsFormatData.statewise[28].state;
            document.getElementById("cc1").innerHTML = jsFormatData.statewise[28].confirmed;
            document.getElementById("cc2").innerHTML = jsFormatData.statewise[28].recovered;
            document.getElementById("cc3").innerHTML = jsFormatData.statewise[28].deaths;
            document.getElementById("cc4").innerHTML = jsFormatData.statewise[28].lastupdatedtime;


            document.getElementById("dd").innerHTML = jsFormatData.statewise[29].state;
            document.getElementById("dd1").innerHTML = jsFormatData.statewise[29].confirmed;
            document.getElementById("dd2").innerHTML = jsFormatData.statewise[29].recovered;
            document.getElementById("dd3").innerHTML = jsFormatData.statewise[29].deaths;
            document.getElementById("dd4").innerHTML = jsFormatData.statewise[29].lastupdatedtime;


            document.getElementById("cc").innerHTML = jsFormatData.statewise[30].state;
            document.getElementById("cc1").innerHTML = jsFormatData.statewise[30].confirmed;
            document.getElementById("cc2").innerHTML = jsFormatData.statewise[30].recovered;
            document.getElementById("cc3").innerHTML = jsFormatData.statewise[30].deaths;
            document.getElementById("cc4").innerHTML = jsFormatData.statewise[30].lastupdatedtime;




            document.getElementById("ee").innerHTML = jsFormatData.statewise[32].state;
            document.getElementById("ee1").innerHTML = jsFormatData.statewise[32].confirmed;
            document.getElementById("ee2").innerHTML = jsFormatData.statewise[32].recovered;
            document.getElementById("ee3").innerHTML = jsFormatData.statewise[32].deaths;
            document.getElementById("ee4").innerHTML = jsFormatData.statewise[32].lastupdatedtime;

            document.getElementById("ff").innerHTML = jsFormatData.statewise[33].state;
            document.getElementById("ff1").innerHTML = jsFormatData.statewise[33].confirmed;
            document.getElementById("ff2").innerHTML = jsFormatData.statewise[33].recovered;
            document.getElementById("ff3").innerHTML = jsFormatData.statewise[33].deaths;
            document.getElementById("ff4").innerHTML = jsFormatData.statewise[33].lastupdatedtime;


            document.getElementById("gg").innerHTML = jsFormatData.statewise[34].state;
            document.getElementById("gg1").innerHTML = jsFormatData.statewise[34].confirmed;
            document.getElementById("gg2").innerHTML = jsFormatData.statewise[34].recovered;
            document.getElementById("gg3").innerHTML = jsFormatData.statewise[34].deaths;
            document.getElementById("gg4").innerHTML = jsFormatData.statewise[34].lastupdatedtime;

            document.getElementById("hh").innerHTML = jsFormatData.statewise[35].state;
            document.getElementById("hh1").innerHTML = jsFormatData.statewise[35].confirmed;
            document.getElementById("hh2").innerHTML = jsFormatData.statewise[35].recovered;
            document.getElementById("hh3").innerHTML = jsFormatData.statewise[35].deaths;
            document.getElementById("hh4").innerHTML = jsFormatData.statewise[35].lastupdatedtime;


            document.getElementById("ii").innerHTML = jsFormatData.statewise[36].state;
            document.getElementById("ii1").innerHTML = jsFormatData.statewise[36].confirmed;
            document.getElementById("ii2").innerHTML = jsFormatData.statewise[36].recovered;
            document.getElementById("ii3").innerHTML = jsFormatData.statewise[36].deaths;
            document.getElementById("ii4").innerHTML = jsFormatData.statewise[36].lastupdatedtime;


            document.getElementById("jj").innerHTML = jsFormatData.statewise[37].state;
            document.getElementById("jj1").innerHTML = jsFormatData.statewise[37].confirmed;
            document.getElementById("jj2").innerHTML = jsFormatData.statewise[37].recovered;
            document.getElementById("jj3").innerHTML = jsFormatData.statewise[37].deaths;
            document.getElementById("jj4").innerHTML = jsFormatData.statewise[37].lastupdatedtime;

        }
        getcovidApi();
    </script>
    <div align="center">
        <hr>
        <h1 style="color:#03256c;">covid-19 LIVE STATUS</h1>
        <hr>

        <div class="container">

            <div class="row India">
                <div class="col-lg-4 col-md-4">
                    <div class="content1">
                        <h3>CONFIRMED</h3>
                        <p id="a1"> </p>
                    </div>
                </div>
                <div class="col-lg-4 col-md-4">
                    <div class="content1">
                        <h3>RECOVERED</h3>
                        <p id="a2"> </p>
                    </div>
                </div>
                <div class="col-lg-4 col-md-4">
                    <div class="content1">
                        <h3>DEATHS</h3>
                        <p id="a3"> </p>
                    </div>
                </div>
            </div>
        </div>

        <table class="table-responsive-sm">
            <thead>
                <tr style="background-color:#ff8303;">
                    <th style="padding:10px">NAME</th>
                    <th style="padding: 10px">CONFIRMED</th>
                    <th style="padding:10px">RECOVERED</th>
                    <th style="padding:10px">DEATHS</th>
                    <th style="padding:10px">UPDATED TIME</th>
                </tr>
            </thead>
            <br>
            <tbody class="bg-active">

                <tr>
                    <td style="padding:10px">
                        <p id="b"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="b1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="b2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="b3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="b4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="c"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="c1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="c2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="c3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="c4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="d"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="d1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="d2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="d3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="d4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="e"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="e1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="e2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="e3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="e4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="f"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="f1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="f2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="f3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="f4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="g"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="g1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="g2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="g3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="g4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="h"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="h1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="h2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="h3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="h4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="i"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="i1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="i2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="i3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="i4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="j"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="j1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="j2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="j3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="j4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="k"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="k1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="k2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="k3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="k4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="l"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="l1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="l2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="l3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="l4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="m"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="m1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="m2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="m3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="m4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="n"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="n1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="n2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="n3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="n4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="o"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="o1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="o2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="o3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="o4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="p"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="p1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="p2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="p3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="p4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="q"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="q1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="q2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="q3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="q4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="r"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="r1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="r2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="r3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="r4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="s"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="s1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="s2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="s3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="s4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="t"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="t1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="t2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="t3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="t4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="u"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="u1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="u2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="u3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="u4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="v"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="v1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="v2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="v3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="v4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="w"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="w1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="w2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="w3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="w4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="x"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="x1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="x2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="x3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="x4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="y"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="y1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="y2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="y3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="y4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="z"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="z1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="z2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="z3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="z4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="aa"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="aa1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="aa2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="aa3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="aa4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="bb"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="bb1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="bb2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="bb3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="bb4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="cc"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="cc1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="cc2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="cc3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="cc4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="dd"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="dd1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="dd2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="dd3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="dd4"> </p>
                    </td>
                </tr>

                <tr>
                    <td style="padding:10px">
                        <p id="ee"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="ee1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="ee2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="ee3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="ee4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="ff"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="ff1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="ff2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="ff3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="ff4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="gg"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="gg1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="gg2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="gg3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="gg4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="hh"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="hh1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="hh2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="hh3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="hh4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="ii"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="ii1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="ii2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="ii3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="ii4"> </p>
                    </td>
                </tr>
                <tr>
                    <td style="padding:10px">
                        <p id="jj"></p>
                    </td>
                    <td style="padding:10px">
                        <p id="jj1"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="jj2"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="jj3"> </p>
                    </td>
                    <td style="padding:10px">
                        <p id="jj4"> </p>
                    </td>
                </tr>
            </tbody>
        </table>
        <br>
        <a href="javascript:location.reload(true)"><button class="btn btn-primary">REFRESH PAGE</button></a>
    </div>
    <hr>
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
        integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
        crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
        integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
        crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>
</body>
<footer class="text-muted">
    <div class="container text-center">
        <br>
        <p>HELPLINE NUMBER : +91-11-23978046</p>
        <p>TOLL FREE NUMBER: 1075</p>
        <h5><b>✅STAY HOME,STAY SAFE!!✅</b></h5>
    </div>
</footer>

</html>
