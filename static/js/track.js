// Track License: look up a cylinder's gas type and license by serial number.
(function () {
  var form = document.getElementById('track-form');
  var input = document.getElementById('serial');
  var result = document.getElementById('track-result');
  var cylinders = JSON.parse(document.getElementById('cylinder-data').textContent);

  function findGas(serial) {
    for (var i = 0; i < cylinders.length; i++) {
      var ranges = cylinders[i].ranges;
      for (var j = 0; j < ranges.length; j++) {
        if (serial >= ranges[j][0] && serial <= ranges[j][1]) return cylinders[i];
      }
    }
    return null;
  }

  function show(node) {
    result.innerHTML = '';
    result.appendChild(node);
  }

  function setError(message) {
    input.setAttribute('aria-invalid', message ? 'true' : 'false');
    var hint = document.getElementById('serial-hint');
    hint.textContent = message || "Numbers only. You'll find it stamped on the cylinder.";
    hint.classList.toggle('is-error', !!message);
  }

  function check(raw) {
    var value = String(raw || '').replace(/\s+/g, '');
    if (!value) { setError('Enter the serial number from the cylinder.'); result.innerHTML = ''; return; }
    if (!/^\d+$/.test(value)) { setError('Use numbers only, for example 1234.'); result.innerHTML = ''; return; }
    setError('');

    var serial = parseInt(value, 10);
    var gas = findGas(serial);
    var url = new URL(window.location.href);
    url.searchParams.set('serial', String(serial));
    window.history.replaceState(null, '', url);

    if (!gas) {
      var miss = document.getElementById('tpl-missing').content.cloneNode(true);
      miss.querySelector('.result-text').textContent =
        'There is no cylinder with serial number ' + serial + '. Check the number on the cylinder and try again.';
      show(miss);
      return;
    }

    var found = document.getElementById('tpl-found').content.cloneNode(true);
    found.querySelector('.result-serial').textContent = 'Serial no. ' + serial;
    found.querySelector('.result-gas').textContent = gas.name;
    if (gas.license) {
      found.querySelector('.license-link').href = gas.license;
      var img = found.querySelector('.license-img');
      img.src = gas.license;
      img.alt = gas.name + ' cylinder license';
    } else {
      found.querySelector('.result-license').hidden = true;
      found.querySelector('.result-nolicense').hidden = false;
    }
    show(found);
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    check(input.value);
  });

  // Links such as /track-license?serial=1234 (e.g. from a QR code) show the result straight away.
  var initial = new URLSearchParams(window.location.search).get('serial');
  if (initial) {
    input.value = initial;
    check(initial);
  }
})();
