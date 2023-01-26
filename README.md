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

programmet läser varje rad och lägger den sista ordet i raden i listan eller att den tarvet redan delen som skall översättas till svenska så sätts resten av raden till listan.


syftet med programmet är att göra receptet lite finare men mainly skall den bah behöva göra om måttet till svenska. 
config.json kommer innehålla storleken på new line samt måttens omvandlingar.
hellu