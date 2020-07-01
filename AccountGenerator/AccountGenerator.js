/***************************************************************************************
    
    This script is licensed under the MIT License.
    Copyright (c) 2020 Ray Adams

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    
***************************************************************************************/

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
