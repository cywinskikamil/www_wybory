kandydaci = [];
kandydaci_namespace = { wszystkie_glosy:0, kandydaci };

function drawMap(dataaa) {
    // alert('zxc');
    google.charts.load('current', {'packages': ['geochart']});
    google.charts.setOnLoadCallback(drawRegionsMap);
    var hehe = $("#chart_div_not");
    $(hehe).replaceWith('<div id="chart_div")>hoho</div>');
    function drawRegionsMap() {
        var table = [['State', kandydaci_namespace.kandydaci[0].nazwisko, kandydaci_namespace.kandydaci[1].nazwisko]];
        for (var i = 0; i < dataaa.length; i++) {
            table.push([dataaa[i].nazwa, dataaa[i].suma_glosow[2], dataaa[i].suma_glosow[4]]);
        }
        var data = google.visualization.arrayToDataTable(table);
        var options = {
            region: 'PL',
            displayMode: 'regions',
            resolution: 'provinces',
            colorAxis: {colors: ['orange', 'blue']}
        };

        var chart = new google.visualization.GeoChart(document.getElementById('chart_div'));
        chart.draw(data, options);
    };
}

function pokazKandydats(kandydats) {
    console.log(kandydaci_namespace.wszystkie_glosy);
    var table = '<div id="wyniki">';
    for (var i = 0; i < kandydats.length; i++) {
        kandydaci_namespace.kandydaci[i] = kandydats[i];
        kandydaci_namespace.wszystkie_glosy = kandydats[i].wszystkie_glosy;
        table += '<h3>' + kandydats[i].imie + ' ' + kandydats[i].nazwisko + '</h3>';
        table += '<h4>' + kandydats[i].liczba_glosow + ' <meter id=kandydat_' + i + ' class="kandydat druk" ' +
                'value=' + kandydats[i].liczba_glosow + ' max=' + kandydaci_namespace.wszystkie_glosy + '>' +
                '</meter> ' + Math.round(kandydats[i].liczba_glosow / kandydats[i].wszystkie_glosy * 10000)/100 + '%</h4>';
    }
    table += '</div>';
    return table;
}

function pokazWojewodztwa(wojewodztwa) {
    var suma = 0;
    var pierwszy = 0;
    var table = '<table id="wojewodztwa"><tr><th id="clickable" colspan="5">sdf</th></tr><tr><th rowspan="2" class="mobile">Nazwa</th><th rowspan="2" ' +
            'class="niezawsze">Liczba głosów ważnych</th><th colspan="2" class="kand_mobile">' +
            kandydaci_namespace.kandydaci[0].imie + ' ' + kandydaci_namespace.kandydaci[0].nazwisko +
            '</th><th class="niezawsze" rowspan="2">Liczba głosów: na kandydata/ważnych [%]' +
            '</th><th colspan="2" class="kand_mobile">' + kandydaci_namespace.kandydaci[1].imie + ' ' +
            kandydaci_namespace.kandydaci[1].nazwisko + '</th></tr><tr><th>Liczba</th><th >%</th><th >%</th>' +
            '<th>Liczba</th></tr>';
    for (var i = 0; i < wojewodztwa.length; i++) {
        suma += wojewodztwa[i].suma_glosow[0];
        pierwszy += wojewodztwa[i].suma_glosow[1];
        table += '<tr id="' + wojewodztwa[i].id + '">' +
                '<td class="mobile">' + wojewodztwa[i].nazwa + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[0] + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[1] + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[2] + '</td>' +
                '<td class="niezawsze"><meter id="pojedynek" value="' +
                wojewodztwa[i].suma_glosow[2] +'" max="100"></meter></td>' +
                '<td>' + wojewodztwa[i].suma_glosow[3] + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[4] + '</td>' +
                '</tr>';
    }
    var percent = Math.round(pierwszy / suma * 10000)/100;
    table += '<tr style="color: red"><td class="mobile">RAZEM</td>' +
            '<td>' + suma + '</td>' +
            '<td>' + pierwszy + '</td>' +
            '<td>' + percent  + '</td>' +
            '<td class="niezawsze" ><meter id="pojedynek" value="' +
            percent + '" max="100"></meter></td>' +
            '<td>' + (100 - percent)  + '</td>' +
            '<td>' + (suma - pierwszy) + '</td>' +
            '</tr>';

    table += '</table>';
    return table;
}

function pokazRodzaj(wojewodztwa) {
    var table = '<tr id="rodzaje">';
    for (var i = 0; i < wojewodztwa.length; i++) {
        table += '<tr id="' + wojewodztwa[i].id + '">' +
                '<td class="mobile">' + wojewodztwa[i].rodzaj + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[0] + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[1] + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[2] + '</td>' +
                '<td class="niezawsze"><meter id="pojedynek" value="' +
                wojewodztwa[i].suma_glosow[2] +'" max="100"></meter></td>' +
                '<td>' + wojewodztwa[i].suma_glosow[3] + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[4] + '</td>' +
                '</tr>';
    }
    table += '</tr>';
    return table;
}

function pokazRozmiar(wojewodztwa) {
    var table = '<tr id="rodzaje">';
    for (var i = 0; i < wojewodztwa.length; i++) {
        table += '<tr id="' + wojewodztwa[i].id + '">' +
                '<td class="mobile">Od ' + wojewodztwa[i].dolny_limit + ' do ' + wojewodztwa[i].gorny_limit + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[0] + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[1] + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[2] + '</td>' +
                '<td class="niezawsze"><meter id="pojedynek" value="' +
                wojewodztwa[i].suma_glosow[2] +'" max="100"></meter></td>' +
                '<td>' + wojewodztwa[i].suma_glosow[3] + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[4] + '</td>' +
                '</tr>';
    }
    table += '</tr>';
    return table;
}

function createTable(gminy) {
        var table;
        table = "<table class=\"modal-table\">\
                <tr class=\"woj\" id=\"-1\"><td class=\"woj\" colspan=\"8\">Rozkład głosów w gminach</td></tr>\
                <tr id=\"-1\">\
                    <th>Gmina</th>\
                    <th>Liczba głosów ważnych </th>\
                    <th>Liczba głosów " + kandydats[0].imie + kandydats[0].nazwisko + "</th>\
                    <th>Procent głosów " + kandydats[0].imie + kandydats[0].nazwisko + "</th>\
                    <th>Liczba głosów kandydata/ważnych</th>\
                    <th>Procent głosów" + kandydats[1].imie + kandydats[1].nazwisko + "</th>\
                    <th>Liczba głosów" + kandydats[1].imie + kandydats[1].nazwisko + "</th>\
                    <th></th>\
                </tr>";
        for (var i = 0; i < gminy.length; i++) {
            table +=
            '<tr id="' + gminy[i].id + '" value="' + gminy[i].date + '">\
                <td>' + gminy[i].nazwa + '</td>\
                <td id="all" value="' + gminy[i].valid_votes + '">' + gminy[i].valid_votes + '</td>\
                <td id="c1" value="' + gminy[i].c1 + '">' + gminy[i].c1 + '</td>\
                <td>' + gminy[i].pc1 + '</td>\
                <td><progress class="table" max="' + gminy[i].valid_votes +
                    '" value="' + gminy[i].c1+ '"></progress></td> \
                <td>' + gminy[i].pc2 + '</td>\
                <td id="c2" value="' + gminy[i].c2 + '">' + gminy[i].c2 + '</td> \
                <td>\
                <button type="button" id="modify-button" class="modify-municipality">Modify</button>\
                </td>\
            </tr>'
        }
        table += '</table>';

        return table;
    }

function pokaz_wyniki() {
    var csrftoken = $.cookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.ajax({
        type:'GET',
        url: 'kandydats/',
        contentType: "application/json",
        processData: false,
        dataType: "json",
        success: function(json) {
            var moje_w = $("#wyniki");
            $(moje_w).replaceWith(pokazKandydats(json));
            pokaz_wojewodztwa();
        },
        error: function(){
            alert('nieudalosie');
        }
    });
}

function pokaz_wojewodztwa() {
    var csrftoken = $.cookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.ajax({
        type:'GET',
        url: 'wojewodztwos/',
        contentType: "application/json",
        processData: false,
        dataType: "json",
        success: function(json) {
            // alert('working');
            // console.log('before');
            var moje_w = $("#wojew");
            var kand1 = $("#kand1");
            var kand2 = $("#kand2");
            $(moje_w).replaceWith(pokazWojewodztwa(json));
            $(kand1).replaceWith('<span>' + kandydaci_namespace.kandydaci[0].imie + ' ' +
                    kandydaci_namespace.kandydaci[0].nazwisko + '</span>');
            $(kand2).replaceWith('<span>' + kandydaci_namespace.kandydaci[1].imie + ' ' +
                    kandydaci_namespace.kandydaci[1].nazwisko + '</span>');
            // console.log('after');
            pokaz_rodzaj();
            drawMap(json);
        },
        error: function(){
            alert('nieudalosieeng');
        }
    });
}

function pokaz_rodzaj() {
    var csrftoken = $.cookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.ajax({
        type:'GET',
        url: 'wojewodztwosrodzaj/',
        contentType: "application/json",
        processData: false,
        dataType: "json",
        success: function(json) {
            // alert('nada');
            // console.log('zx');
            var moje_w = $("#rodzaje");
            $(moje_w).replaceWith(pokazRodzaj(json));
            // console.log('cx');
            pokaz_ludnosc();
        },
        error: function(){
            alert('nieudieeng');
        }
    });
}

function pokaz_ludnosc() {
    var csrftoken = $.cookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $.ajax({
        type:'GET',
        url: 'wojewodztwosrozmiar/',
        contentType: "application/json",
        processData: false,
        dataType: "json",
        success: function(json) {
            // alert('feder');
            // console.log('zx');
            var moje_w = $("#ludnosci");
            $(moje_w).replaceWith(pokazRozmiar(json));
            // console.log('cx');
        },
        error: function(){
            alert('nieudieeng');
        }
    });
}

function logFunction() {
var csrftoken = $.cookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$.ajax({
    type:"POST",
    url:"/projekt_zaliczeniowy/login/",
    data: JSON.stringify({
        'username': document.getElementById("login").value,
        'password': document.getElementById("password").value}),
    contentType: "application/json",
    processData: false,
    success:function(data){
        d = JSON.parse(data);
        if (d.action == 'login') {
            if (d.result == 'success') {
                document.getElementById("login").style.display = 'none';
                document.getElementById("password").style.display = 'none';
                document.getElementById("login_button").value = "Wyloguj się";
                alert('Zostałeś pomyślnie zalogowany.');
            } else {
                alert('Błędny login lub hasło.');
            }
        } else {
            document.getElementById("login").style.display = '';
            document.getElementById("password").style.display = '';
            document.getElementById("login_button").value = "Zaloguj się";
            alert('Zostałeś pomyślnie wylogowany.');
        }
    },
    error:function(data){
        alert('POST error');
        console.log(data);
    }
});
}

$(document).ready(function () {
    // function submit(communityId, firstVotes, secondVotes, allVotes, dateModified, result, callback) {
    //     var csrftoken = $.cookie('csrftoken');
    //
    //     function csrfSafeMethod(method) {
    //         // these HTTP methods do not require CSRF protection
    //         return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    //     }
    //
    //     $.ajaxSetup({
    //         beforeSend: function (xhr, settings) {
    //             if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
    //                 xhr.setRequestHeader("X-CSRFToken", csrftoken);
    //             }
    //         }
    //     });
    //
    //     $.ajax({
    //         type: "POST",
    //         url: "/projekt_zaliczeniowy/submit/",
    //         data: JSON.stringify({
    //             'all_votes': allVotes,
    //             'community_id': communityId,
    //             'first_votes': firstVotes,
    //             'second_votes': secondVotes,
    //             'date_modified': dateModified
    //         }),
    //         contentType: "application/json",
    //         processData: false,
    //         success: function (data) {
    //             if (callback) {
    //                 callback(communityId, firstVotes, secondVotes, dateModified, data, result);
    //             }
    //         },
    //         error: function (data) {
    //             alert('POST error');
    //             console.log(data);
    //             result = false;
    //             return;
    //         }
    //     });
    // }

    var modal = document.getElementById('myModal');
    var span = document.getElementsByClassName("close")[0];

    $(".clickable").hover(function () {
        console.log('asd');
    }, function () {
        console.log('zxc');
    });

    $("#cokolwiek").hover(function () {
        console.log('cokolwiek');
    }, function () {

    });

    span.onclick = function () {
        modal.style.display = "none";
    };

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };

    // $("div.modal").on('click', 'button.modify-municipality', function () {
    //     var tr = $(this).closest('tr')
    //     console.log("tr_id", tr.attr('id'));
    //     var td_c1 = tr.children('td#c1');
    //     var td_c2 = tr.children('td#c2');
    //     var alll = tr.children('td#all');
    //
    //     console.log(td_c1.attr('value'));
    //     console.log(td_c2.attr('value'));
    //     console.log(alll.attr('value'));
    //
    //     td_c1.replaceWith('<input id="c1" type="number" value="' + td_c1.attr('value') + '"name="c1">');
    //     td_c2.replaceWith('<input id="c2" type="number" value="' + td_c2.attr('value') + '"name="c2">');
    //     $(this).replaceWith('<input id="submit-municipality" type="submit">');
    // });
    //
    // $("div.modal").on('click', 'input#submit-municipality', function () {
    //     var tr = $(this).closest('tr');
    //     var c1 = tr.find('input#c1');
    //     var c2 = tr.find('input#c2');
    //     var all = tr.children('td#all').attr('value');
    //     var c1_val = c1.val();
    //     var c2_val = c2.val();
    //     $(this).replaceWith('<button type="button" id="modify-button" class="modify-municipality">Modify</button>');
    //
    //     console.log("c1:", c1_val);
    //     console.log("c2:", c2_val);
    //     console.log("all:", all);
    //     console.log("halo halo a id:", tr.attr('id'));
    //     console.log("date:", tr.attr('value'));
    //
    //
    //     var callback = function (communityId, firstVotes, secondVotes, dateModified, data, result) {
    //         console.log(" w callback");
    //         d = JSON.parse(data);
    //         if (d.result == 'success') {
    //             console.log('uwaga, lecimy');
    //             console.log(d.gmina_nazwa);
    //             console.log('data:' + d.date_modified + ' !');
    //             console.log('za tym');
    //             result = true;
    //         } else {
    //             console.log("jestem tutej")
    //             console.log(d.pierwsza);
    //             console.log(d.druga);
    //             result = false;
    //         }
    //
    //         if (result) {
    //             alert("Modyfikacja powiodła się");
    //             c1.replaceWith('<td id="c1"     value="' + c1_val + '">' + c1_val + '</td>');
    //             c2.replaceWith('<td id="c2" value="' + c2_val + '">' + c2_val + '</td>');
    //             tr.attr('value', d.date_modified);
    //         } else {
    //             alert("Modyfikcja nie powiodła się, zamknij modalne okno");
    //         }
    //     };
    //
    //     var result;
    //     submit(tr.attr('id'), c1_val, c2_val, all, tr.attr('value'), result, callback);
    // });
});