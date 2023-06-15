Tanke proccess

projectet skall vara en redigerare för amerikanska recept
vad den skall göra är att omvandla amerikanska mått till svenska 
dessutom skall den kunna dela upp instruktionerna i stycken för bättre läsning, har en ide med att den gör newline efter den hittar en ingridiens med en punkt efter sig.
Dvs måste programmet veta vad en ingidens är och vad en ickerelevant ord är.
Min tanke är att använda en dictionary för att hålla koll på ord och deras betydelse. Eller att använda en lista med ord som är ingridiens, hur jag tänker är mainly basserat på strukturen som t.ex

Ingriens:
1 1/2 cups flour 
1/2 cup sugar
1/2 cup butter
1/2 cup milk
 
 mst ha krav som den tillåter inte negativa tal.
programmet läser varje rad och lägger den sista ordet i raden i listan eller att den tarvet redan delen som skall översättas till svenska så sätts resten av raden till listan.


syftet med programmet är att göra receptet lite finare men mainly skall den bah behöva göra om måttet till svenska. 
config.json kommer innehålla storleken på new line samt måttens omvandlingar.


\d+ matches one or more digits (0-9).
(\.\d+)? matches an optional decimal part preceded by a dot. It captures the decimal part if it exists.
(\d+(\.\d+)?) matches the whole number, including an optional decimal part.
ounces matches the literal string "ounces" following the number.
So, the regular expression pattern (\d+(\.\d+)?) ounces will match values like "2 ounces", "1.5 ounces", "0.25 ounces", etc., in the input file.

When using re.findall() with this pattern, it will find all occurrences of the pattern in the file and return a list of matched values.