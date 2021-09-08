useful regex patterns

html : (?:<style.+?>.+?</style>|<script.+?>.+?</script>|<(?:!|/?[a-zA-Z]+).*?/?>)

in between : (.*?\n*)* 

Cheat Sheet – Regex Rules
Character classes		Quantifiers & Alternation	
.	any character except newline	a* a+ a?	0 or more, 1 or more, 0 or 1
\w \d \s	word, digit, whitespace	a{5} a{2,}	exactly five, two or more
\W \D \S	not word, digit, whitespace	a{1,3}	between one & three
[abc]	any of a, b, or c	a+? a{2,}?	match as few as possible
[^abc]	not a, b, or c	ab|cd	match ab or cd
[a-g]	character between a & g		
Anchors		Groups & Lookaround	
^abc$	start / end of the string	(abc)	capture group
\b	word boundary	\1	backreference to group #1
Escaped characters		(?:abc)	non-capturing group
\. \* \\	\ is used to escape special chars. \* matches *	(?=abc)	positive lookahead
\t \n \r	tab, linefeed, carriage return	(?!abc)	negative lookahead
Commonly used Regex
1. Digits
Whole Numbers – /^\d+$/
Decimal Numbers – /^\d*\.\d+$/
Whole + Decimal Numbers – /^\d*(\.\d+)?$/
Negative, Positive Whole + Decimal Numbers – /^-?\d*(\.\d+)?$/
Whole + Decimal + Fractions – /[-]?[0-9]+[,.]?[0-9]*([\/][0-9]+[,.]?[0-9]*)*/
2. Alphanumeric Characters
Alphanumeric without space – /^[a-zA-Z0-9]*$/
Alphanumeric with space – /^[a-zA-Z0-9 ]*$/
3. Email
Common email Ids – /^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})*$/
Uncommon email ids – /^([a-z0-9_\.\+-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/
4. Password Strength
Complex: Should have 1 lowercase letter, 1 uppercase letter, 1 number, 1 special character and be at least 8 characters long
/(?=(.*[0-9]))(?=.*[\!@#$%^&*()\\[\]{}\-_+=~`|:;"'<>,./?])(?=.*[a-z])(?=(.*[A-Z]))(?=(.*)).{8,}/ 
Moderate: Should have 1 lowercase letter, 1 uppercase letter, 1 number, and be at least 8 characters long
/(?=(.*[0-9]))((?=.*[A-Za-z0-9])(?=.*[A-Z])(?=.*[a-z]))^.{8,}$/
5. Username
Alphanumeric string that may include _ and – having a length of 3 to 16 characters –
/^[a-z0-9_-]{3,16}$/
6. URL
Include http(s) Protocol
/https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#()?&//=]*)/ 
Protocol Optional
/(https?:\/\/)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/ 
7. IP Address
IPv4 address
IPv6 address
Both IPv4, IPv6 addresses
1
2
3
4
5
6
/* Match IPv4 address */
/^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$/ 
/* Match IPv6 address */
/(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))/
/* Match both IPv4, IPv6 addresses */
/((^\s*((([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))\s*$)|(^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$))/
8. Dates
Date Format YYYY-MM-dd using separator -
Date Format dd-MM-YYYY using separators - or . or /
Date Format dd-mmm-YYYY using separators - or . or /
1
2
3
4
5
6
7
8
9
10
11
12
13
/* Date Format YYYY-MM-dd */
/([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))/
 
/* Date Format dd-MM-YYYY or 
               dd.MM.YYYY or
               dd/MM/YYYY
   with check for leap year */
/^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$/
 
/* Date Format dd-mmm-YYYY or
               dd/mmm/YYYY or
               dd.mmm.YYYY */
/^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]|(?:Jan|Mar|May|Jul|Aug|Oct|Dec)))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2]|(?:Jan|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec))\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)(?:0?2|(?:Feb))\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9]|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep))|(?:1[0-2]|(?:Oct|Nov|Dec)))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$/
9. Time
Time Format HH:MM 12-hour, optional leading 0
/^(0?[1-9]|1[0-2]):[0-5][0-9]$/
Time Format HH:MM 12-hour, optional leading 0, Meridiems (AM/PM)
/((1[0-2]|0?[1-9]):([0-5][0-9]) ?([AaPp][Mm]))/
Time Format HH:MM 24-hour with leading 0
/^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/
Time Format HH:MM 24-hour, optional leading 0
/^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/
Time Format HH:MM:SS 24-hour
/(?:[01]\d|2[0123]):(?:[012345]\d):(?:[012345]\d)/
10. HTML Tags
Elements with Attributes /<\/?[\w\s]*>|<.+[\W]>/
11. Javascript Handlers
Inline JS handler /\bon\w+=\S+(?=.*>)/
Inline JS handler with element /(?:<[^>]+\s)(on\S+)=["']?((?:.(?!["']?\s+(?:\S+)=|[>"']))+.)["']?/
12. Slug
Slug /^[a-z0-9]+(?:-[a-z0-9]+)*$/
13. Match Duplicates in a String
Search Duplicates /(\b\w+\b)(?=.*\b\1\b)/
14. Phone Numbers
International Phone Numbers – with optional country code/extension
1
2
/* International Phone Numbers */
/^(?:(?:\(?(?:00|\+)([1-4]\d\d|[1-9]\d?)\)?)?[\-\.\ \\\/]?)?((?:\(?\d{1,}\)?[\-\.\ \\\/]?){0,})(?:[\-\.\ \\\/]?(?:#|ext\.?|extension|x)[\-\.\ \\\/]?(\d+))?$/
Note: Use regex for validating phone numbers only if you don’t have the choice to use a library. There are several libraries that handle phone numbers more accurately and should be used instead.

15. File Path
File Path with Filename and extension
/((\/|\\|\/\/|https?:\\\\|https?:\/\/)[a-z0-9 _@\-^!#$%&+={}.\/\\\[\]]+)+\.[a-z]+$/
File Path with optional Filename, extension
/^(.+)/([^/]+)$/
File Name with extension having 3 chars
/^[\w,\s-]+\.[A-Za-z]{3}$/
Additional Regexes
1. Zip codes
There is NO single Regex that can handle all zip codes given that zip codes around the world do not follow a common pattern. Here is a list that contains Regex specific to each country.

2. Payment Validation
Here is a link that contains regex for validating leading Credit cards like Visa, Mastercard and so on.

3. Identity Documents
Social Security Number – Ref
/* can use either hypen(-) or space( ) character as separator */
/^((?!219-09-9999|078-05-1120)(?!666|000|9\d{2})\d{3}-(?!00)\d{2}-(?!0{4})\d{4})|((?!219 09 9999|078 05 1120)(?!666|000|9\d{2})\d{3} (?!00)\d{2} (?!0{4})\d{4})|((?!219099999|078051120)(?!666|000|9\d{2})\d{3}(?!00)\d{2}(?!0{4})\d{4})$/
Passport – /^[A-PR-WY][1-9]\d\s?\d{4}[1-9]$/


