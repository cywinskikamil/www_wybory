kandydaci = [];
kandydaci_namespace = { wszystkie_glosy:0, kandydaci };

function acutalPercent(part, all) {
    return Math.round(part * 10000 / all)/100;
}

function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function updateMap(dataaa) {
    google.charts.setOnLoadCallback(drawRegionsMap)
    var hehe = $("#chart_div_not");
    $(hehe).replaceWith('<div id="chart_div")></div>');
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
    }
}

function drawMap() {
    google.charts.load('current', {'packages': ['geochart']});
}

function pokazKandydats(kandydats) {
    // console.log(kandydaci_namespace.wszystkie_glosy);
    var table = '<div id="wyniki">';
    for (var i = 0; i < kandydats.length; i++) {
        kandydaci_namespace.kandydaci[i] = kandydats[i];
        kandydaci_namespace.wszystkie_glosy = kandydats[i].wszystkie_glosy;
        table += '<h3>' + kandydats[i].imie + ' ' + kandydats[i].nazwisko + '</h3>';
        table += '<h4>' + kandydats[i].liczba_glosow + ' <meter id=kandydat_' + i + ' class="kandydat druk" ' +
                'value=' + kandydats[i].liczba_glosow + ' max=' + kandydaci_namespace.wszystkie_glosy + '>' +
                '</meter> ' + acutalPercent(kandydats[i].liczba_glosow, kandydats[i].wszystkie_glosy) + '%</h4>';
    }
    table += '</div>';
    return table;
}

function pokazWojewodztwa(wojewodztwa) {
    var suma = 0;
    var pierwszy = 0;
    var table = '<table id="wojew"><tr><th rowspan="2" class="mobile">Nazwa</th><th rowspan="2" ' +
            'class="niezawsze">Liczba głosów ważnych</th><th colspan="2" class="kand_mobile">' +
            kandydaci_namespace.kandydaci[0].imie + ' ' + kandydaci_namespace.kandydaci[0].nazwisko +
            '</th><th class="niezawsze" rowspan="2">Liczba głosów: na kandydata/ważnych [%]' +
            '</th><th colspan="2" class="kand_mobile">' + kandydaci_namespace.kandydaci[1].imie + ' ' +
            kandydaci_namespace.kandydaci[1].nazwisko + '</th></tr><tr><th>Liczba</th><th >%</th><th >%</th>' +
            '<th>Liczba</th></tr>';
    for (var i = 0; i < wojewodztwa.length; i++) {
        suma += wojewodztwa[i].suma_glosow[0];
        pierwszy += wojewodztwa[i].suma_glosow[1];
        table += '<tr id="' + wojewodztwa[i].id + '" class="clickable-woj">' +
                '<td class="mobile">' + wojewodztwa[i].nazwa + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[0] + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[1] + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[2] + '</td>' +
                '<td class="niezawsze"><meter id="pojedynek" value="' +
                wojewodztwa[i].suma_glosow[2] +'" max="100"></meter></td>' +
                '<td>' + wojewodztwa[i].suma_glosow[4] + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[3] + '</td>' +
                '</tr>';
    }
    var percent = acutalPercent(pierwszy, suma);
    // console.log((100 - percent));
    table += '<tr style="color: red"><td class="mobile">RAZEM</td>' +
            '<td>' + suma + '</td>' +
            '<td>' + pierwszy + '</td>' +
            '<td>' + percent  + '</td>' +
            '<td class="niezawsze" ><meter id="pojedynek" value="' +
            percent + '" max="100"></meter></td>' +
            '<td>' + (100 - percent).toFixed(2)  + '</td>' +
            '<td>' + (suma - pierwszy) + '</td>' +
            '</tr>';

    table += '</table>';
    return table;
}

function pokazRodzaj(wojewodztwa) {
    var kandydaci = kandydaci_namespace.kandydaci;
    var table = '<table id="rodzaje"><tr><th id="asdf" rowspan="2" >Podział</th><th rowspan="2" class="niezawsze">' +
                'Liczba głosów ważnych</th><th colspan="2"><span id="kand1">' +
                kandydaci[0].imie + ' ' + kandydaci[0].nazwisko +
                '</span></th>' +
                '<th class="niezawsze" rowspan="2">Liczba głosów: na kandydata/ważnych [%]</th>' +
                '<th colspan="2"><span id="kand2">' +
                kandydaci[1].imie + ' ' + kandydaci[1].nazwisko +
                '</span></th></tr><tr><th>Liczba</th><th>%</th>' +
                '<th>%</th><th>Liczba</th></tr>';    for (var i = 0; i < wojewodztwa.length; i++) {
        table += '<tr id="' + wojewodztwa[i].id + '" class="clickable-rodzaj">' +
                '<td class="mobile">' + wojewodztwa[i].rodzaj + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[0] + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[1] + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[2] + '</td>' +
                '<td class="niezawsze"><meter id="pojedynek" value="' +
                wojewodztwa[i].suma_glosow[2] +'" max="100"></meter></td>' +
                '<td>' + wojewodztwa[i].suma_glosow[4] + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[3] + '</td>' +
                '</tr>';
    }
    table += '</table>';
    return table;
}

function pokazRozmiar(wojewodztwa) {
    var kandydaci = kandydaci_namespace.kandydaci;
    var table = '<table id="ludnosci"><tr><th id="asdf" rowspan="2" >Podział</th><th rowspan="2" class="niezawsze">' +
                'Liczba głosów ważnych</th><th colspan="2"><span id="kand1">' +
                kandydaci[0].imie + ' ' + kandydaci[0].nazwisko +
                '</span></th>' +
                '<th class="niezawsze" rowspan="2">Liczba głosów: na kandydata/ważnych [%]</th>' +
                '<th colspan="2"><span id="kand2">' +
                kandydaci[1].imie + ' ' + kandydaci[1].nazwisko +
                '</span></th></tr><tr><th>Liczba</th><th>%</th>' +
                '<th>%</th><th>Liczba</th></tr>';
    for (var i = 0; i < wojewodztwa.length; i++) {
        table += '<tr id="' + wojewodztwa[i].id + '" class="clickable-rozmiar">' +
                '<td class="mobile">Od ' + wojewodztwa[i].dolny_limit + ' do ' + wojewodztwa[i].gorny_limit + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[0] + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[1] + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[2] + '</td>' +
                '<td class="niezawsze"><meter id="pojedynek" value="' +
                wojewodztwa[i].suma_glosow[2] +'" max="100"></meter></td>' +
                '<td>' + wojewodztwa[i].suma_glosow[4] + '</td>' +
                '<td>' + wojewodztwa[i].suma_glosow[3] + '</td>' +
                '</tr>';
    }
    table += '</table>';
    return table;
}

function createTable(gminy) {
        var table;
        var kandydats = kandydaci_namespace.kandydaci;
        table = '<table class="modal-table">' +
                '<tr class="woj" id="-1"><td class="woj" colspan="8">Rozkład głosów w gminach</td></tr>' +
                '<tr id="-1">' +
                    '<th>Gmina</th>' +
                    '<th>Liczba głosów ważnych </th>' +
                    '<th>Liczba głosów ' + kandydats[0].imie + ' ' + kandydats[0].nazwisko + '</th>' +
                    '<th>% głosów ' + kandydats[0].imie + ' ' + kandydats[0].nazwisko + '</th>' +
                    '<th>Liczba głosów kandydata/ważnych</th>' +
                    '<th>% głosów ' + kandydats[1].imie + ' ' + kandydats[1].nazwisko + '</th>' +
                    '<th>Liczba głosów ' + kandydats[1].imie + ' ' + kandydats[1].nazwisko + '</th>' +
                    '<th></th>' +   
                '</tr>';
        for (var i = 0; i < gminy.length; i++) {
            var pierwszy = gminy[i].liczba_glosow_oddanych_na_kandydata_nr_1;
            var drugi = gminy[i].liczba_glosow_oddanych_na_kandydata_nr_2;
            var suma = pierwszy + drugi;
            var procent1 = acutalPercent(pierwszy, suma);
            var procent2 = acutalPercent(drugi, suma);
            table +=
            '<tr id="' + gminy[i].id + '" value="' + gminy[i].data_modyfikacji + '">' +
                '<td id="nazwa" value="' + gminy[i].nazwa + '">' + gminy[i].nazwa + '</td>' +
                '<td id="all" value="' + gminy[i].liczba_wydanych_kart + '">' + gminy[i].liczba_wydanych_kart+ '</td>' +
                '<td id="c1" value="' + pierwszy + '">' + pierwszy + '</td>' +
                '<td id="p1">' + procent1 + '</td>' +
                '<td><progress id="procenty" class="table" max="' + gminy[i].liczba_wydanych_kart +'" value="' + pierwszy + '"></progress>' +
                '</td>' +
                '<td id="p2">' + procent2 + '</td>' +
                '<td id="c2" value="' + drugi + '">' + drugi + '</td> ' +
                '<td id="woj_number" value="' + gminy[i].wojewodztwo_id + '">' +
                '<button type="button" id="modify-button" class="modify-municipality">Modify</button>' +
                '</td>' +
            '</tr>'
        }
        table += '</table>';

        return table;
    }

function pokaz_wyniki() {
    var csrftoken = $.cookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    // console.log('wyniki');
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

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    // console.log('wojewodztwa');
    $.ajax({
        type:'GET',
        url: 'wojewodztwos/',
        contentType: "application/json",
        processData: false,
        dataType: "json",
        success: function(json) {
            var moje_w = $("#wojew");
            $(moje_w).replaceWith(pokazWojewodztwa(json));
            pokaz_rodzaj();
            updateMap(json);
        },
        error: function(){
            alert('nieudalosieeng');
        }
    });
}

function pokaz_rodzaj() {
    var csrftoken = $.cookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    // console.log('rodzaj');
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
            pokaz_ludnosc();
        },
        error: function(){
            alert('nieudieeng');
        }
    });
}

function pokaz_ludnosc() {
    var csrftoken = $.cookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    // console.log('ludnosc');
    $.ajax({
        type:'GET',
        url: 'wojewodztwosrozmiar/',
        contentType: "application/json",
        processData: false,
        dataType: "json",
        success: function(json) {
            var moje_w = $("#ludnosci");
            $(moje_w).replaceWith(pokazRozmiar(json));
        },
        error: function(){
            alert('nieudieeng');
        }
    });
}

$(document).ready(function () {
    drawMap();
    // console.log('uwaga');
    // console.log(acutalPercent(2, 3));
    var modal = document.getElementById('myModal');
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };


    function submit(communityId, firstVotes, secondVotes, allVotes, dateModified, wojew, nazwa, result, callback) {
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
            type:"PUT",
            url: document.URL + 'gminas/' + communityId + '/',
            data: JSON.stringify({
                'wojewodztwo': wojew,
                'id': communityId,
                'nazwa': nazwa,
                'liczba_wydanych_kart': allVotes,
                'liczba_glosow_oddanych_na_kandydata_nr_1': firstVotes,
                'liczba_glosow_oddanych_na_kandydata_nr_2': secondVotes,
                'data_modyfikacji': dateModified}),
            contentType: "application/json",
            processData: false,
            success:function(data){
                console.log('tutaj');
                console.log(dateModified);
                if(callback) {
                    callback(firstVotes, secondVotes, allVotes);
                }
            },
            error:function(data){
                var alerto = data.responseJSON['non_field_errors'][0];
                // console.log(alerto);
                alert(alerto);
                result = false;
                return;
            },

        });
    }


    $("div.modal").on('click', 'button.modify-municipality', function() {
        var tr = $(this).closest('tr')
        var td_c1 = tr.children('td#c1');
        var td_c2 = tr.children('td#c2');
        
        td_c1.replaceWith('<input id="c1" type="number" value="' + td_c1.attr('value') + '"name="c1">');
        td_c2.replaceWith('<input id="c2" type="number" value="' + td_c2.attr('value') + '"name="c2">');
        $(this).replaceWith('<input id="submit-municipality" type="submit">');
    });

    $("div.modal").on('click', 'input#submit-municipality', function() {
        var tr = $(this).closest('tr');
        var c1 = tr.find('input#c1');
        var c2 = tr.find('input#c2');
        var p1 = tr.find('td#p1');
        var p2 = tr.find('td#p2');
        var all = tr.children('td#all').attr('value');
        var procenty = tr.find('progress#procenty');
        var c1_val = c1.val();
        var c2_val = c2.val();
        var wojew = tr.children('td#woj_number').attr('value');
        var nazwa = tr.children('td#nazwa').attr('value');
        $(this).replaceWith('<button type="button" id="modify-button" class="modify-municipality">Modify</button>');

        var callback = function(firstVotes, secondVotes, dateModified) {
            console.log(" w callback");

            c1.replaceWith('<td id="c1" value="' + firstVotes + '">' + firstVotes + '</td>');
            c2.replaceWith('<td id="c2" value="' + secondVotes + '">' + secondVotes + '</td>');
            procenty.attr('value', firstVotes);

            var procent = acutalPercent(firstVotes, +firstVotes + +secondVotes).toFixed(2);
            p1.replaceWith('<td id="p1">' + procent + '</td>');
            p2.replaceWith('<td id="p2">' + (100 - procent).toFixed(2) + '</td>');
            tr.attr('value', dateModified);
            pokaz_wyniki();
        };

        var result;
        submit(tr.attr('id'), c1_val, c2_val, all, tr.attr('value'), wojew, nazwa, result, callback);
    });

});

