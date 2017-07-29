var BOARD_COUNT = 0;
var ROWS_PER_BOARD = 2;
var DIGITS_PER_ROW_PER_BOARD = 4;
var DIGITS_PER_BOARD = ROWS_PER_BOARD * DIGITS_PER_ROW_PER_BOARD;
var DRIVERS_PER_BOARD = DIGITS_PER_BOARD + 1;
var SEGMENTS_PER_DIGIT = 16;
var LEDS_PER_BOARD = 8
var SEGMENT_NAMES = "gtsuhkmabncprdfex";

function update(frame) {
    for (var boardId = 0; boardId < BOARD_COUNT; boardId++) {
        var start, end;

        start = DIGITS_PER_ROW_PER_BOARD * boardId;
        end = DIGITS_PER_ROW_PER_BOARD * (boardId + 1);
        updateRow(boardId, 0, frame.rows[0].slice(start, end));
        updateRow(boardId, 1, frame.rows[1].slice(start, end));

        start = LEDS_PER_BOARD * boardId;
        end = LEDS_PER_BOARD * (boardId + 1);
        updateLeds(boardId, frame.leds.slice(start, end));
    }
}

function updateRow(boardId, rowId, segments) {
    for (var digitId = 0; digitId < DIGITS_PER_ROW_PER_BOARD; digitId++) {
        updateDigit(boardId, rowId, digitId, segments[digitId]);
    }
}

function updateDigit(boardId, rowId, digitId, segments) {
    for (var segmentNameIndex = 0; segmentNameIndex < SEGMENT_NAMES.length; segmentNameIndex++) {
        var segmentName = SEGMENT_NAMES[segmentNameIndex];
        updateDisplaySegment(boardId, rowId, digitId, segmentName, segments[segmentName]);
    }
}

function updateDisplaySegment(boardId, rowId, digitId, segmentName, enabled) {
    var $board = $('.board.b-' + boardId);
    var $digit = $board.find('.d-' + rowId + '-' + digitId);
    var $segment = $digit.find('#' + segmentName);
    $segment.toggleClass('enabled', enabled);
}

function updateLeds(boardId, leds) {
    for (var ledId = 0; ledId < LEDS_PER_BOARD; ledId++) {
        updateLed(boardId, ledId, leds[ledId]);
    }
}

function updateLed(boardId, ledId, enabled) {
    var $board = $('.board.b-' + boardId);
    var $led = $board.find('.l-' + ledId);
    var $path = $led.find('path');
    $path.toggleClass('enabled', enabled);
}


function generateDigit(rowId, displayId) {
    var $display = $('<div class="digit">')
        .data('row-id', rowId)
        .data('display-id', displayId);

    var topRow = (rowId === 0);
    $('<img src="/display/display.svg" class="svg">')
        .addClass(topRow ? 'green' : 'red')
        .addClass('d-' + rowId + '-' + displayId)
        .appendTo($display)
        .svgToInline();

    return $display;

}

function generateLed(ledId) {
    var $led = $('<div class="led">')
        .data('id', ledId);

    $('<img src="/display/led.svg" class="svg red">')
        .addClass('l-' + ledId)
        .appendTo($led)
        .svgToInline();

    return $led;

}

function generateBoard(boardId) {
    var $board = $('<div class="board">')
        .addClass('b-' + boardId)
        .data('id', boardId);

    for (var rowId = 0; rowId < ROWS_PER_BOARD; rowId++) {
        for (var digitId = 0; digitId < DIGITS_PER_ROW_PER_BOARD; digitId++) {
            generateDigit(rowId, digitId)
                .appendTo($board);
        }
    }

    var LEDS = 8;
    for (var ledId = 0; ledId < LEDS; ledId++) {
        generateLed(ledId)
            .appendTo($board);
    }

    return $board
}

function generateHtml(boardCount) {
    var $scroller = $('body > .scroller').empty();
    if ($scroller.length === 0) {
        $scroller = $('<div class="scroller">')
            .appendTo($('body'));
    }

    var $container = $('<div class="preview">')
        .appendTo($scroller)
        .css('width', 994 * boardCount);

    for (var boardId = 0; boardId < boardCount; boardId++) {
        generateBoard(boardId)
            .appendTo($container);
    }
}

$(function () {
    var socket = io.connect('http://' + document.domain + ':' + location.port);
    window.socket = socket;

    socket.on('setup', function (data) {
        console.log('setup');
        generateHtml(data.boardCount);
        BOARD_COUNT = data.boardCount;
        data.clientPlugins.forEach(function (clientPlugin) {
            $.getScript('/plugins/' + clientPlugin + '.js');
        });
    });

    socket.on('frame', function (frame) {
        console.log("received", frame);
        update(frame);
    });
});
