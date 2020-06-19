(async function(){
  var baseUsername = prompt('Enter base username:');
  var password = prompt('Enter password:');
  var amount = prompt('Enter the amount of accounts:');

  var i;
  for (i = 0; i < parseInt(amount); i++) {
    await fetch("https://www.nitrotype.com/api/register", {
      "credentials": "include",
      "headers": {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Prefer": "safe",
        "Content-Type": "application/x-www-form-urlencoded"
      },
    "referrer": "https://www.nitrotype.com/signup",
    "body": "acceptPolicy=true&email=&password=" + password + "&receiveContact=&username=" + baseUsername + i,
    "method": "POST",
    "mode": "cors"
    });
  };
  
  alert('Generating ' + amount + ' accounts... Please wait a couple seconds before leaving the current page.');
})();
