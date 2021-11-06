var bgp = chrome.extension.getBackgroundPage()
var arr = []; // the array

document.addEventListener('DOMContentLoaded', documentEvents, false);

function myAction(input) {
  var lText = input.value
  if (/https:\/\/url.avanan.click\/v2\//.test(lText)) {
    var reg = /https:\/\/url.avanan.click\/v2\/___(.*)___\..*/;
    var url = lText.match(reg)[1];
    bgp.copyToClipboard(url)
  } 
};

function documentEvents() {
  document.getElementById('btcopy').addEventListener('click',
    function() {
      myAction(document.getElementById('tbinput'));
    });
}
