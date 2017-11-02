# NikonLensComparison

## Overview
This project is about comparing DSLR Lenses from every brand and hopefully from every timeline.
With all necessary data without the price.

### Attributes of each Lens
Each Entry has:

Entry                 Description of data (example)
1. Full Lens Name-----"Nikon 8-15mm 1:3.5-4.5E ED AF-S VR"
2. Focal Length Start--8mm
3. Focal Length End---15mm
4. Apeture Start-------3.5
5. Apeture End--------4.5
6. Filtersize------------77mm 
7. Magnification------1:4
8. Mount--------------Nikon F
9. Sensor--------------APS-C /Kleinbild
10. Weight-------------Gramm
11. Size-----------------Diagramm x Length 



## Task List
- [ ] \(Must-Have)----(Never done) Create UML graphs and keep them updated
- [ ] \(Must-Have)----Complete README file
- [x] \(Must-Have)----Got all necessary data from the most Nikon F compatible lenses
- [x] \(Must-Have)----Made a nice GUI for filtering and comparing the lenses (perhaps something like on "geizhals.de") 
- [x] \(Must-Have)----RawData will be shown in the Result Table, if they match the selected / active filters.
- [ ] \(Should-Have)--Able to copy the data from "WebCrawler/rawData.csv" to "AllLenses.xlsm" in the RawData sheet.
- [ ] \(Should-Have)--Create or find Key, so Data about the same lens comes together and so doesn't creates multiple entries.
- [ ] \(Should-Have)--Got all necessary data from ALL the Nikon F compatible lenses
- [ ] \(Should-Have)--Data of Autofocus (AF,AF-S,MF) and Vibration Reduction
- [ ] \(Should-Have)--A Sheet with a Table where you can compare (from the ResultTable) selected lenses.
- [ ] \(NiceTo-Have)--Move from Excel to a real database (e.g. Wide-Column?)
- [ ] \(NiceTo-Have)--Complete standalone program.
- [x] \(NiceTo-Have)--Not only Nikon F lenses, but all Lenses compatible to Nikon F (e.g. with adapter the Pentax Lenses)
- [ ] \(NiceTo-Have)--Sheet with a Table with alle the lenses someone ownes, to see how much you can do with them and if you really need a new lens.
- [ ] \(NiceTo-Have)--Not only Nikon F Lenses and Nikon F compatible lenses, but all Lenses every made.

## Motivation
I really enjoy comparing all the lenses out there.
But on "geizhals.de" you just can compare all lenses which are in stock at the moment.
So all of the good old glas and perhaps one or the other pearl is missing in that list.
I didn't find such a list, so here I will build my own. 

Also I want to practice how to document a project well so everybody could understand it.

## Code Example
TODO

## Installation
To see or edit the UML diagrams go to [draw.io](https://draw.io).
To see or edit the Excel sheet, you will need Microsoft Excel, I use Office 365.
Python is Python 3.
Run the WebCrawler with 'python StartCrawling.py' in the WebCrawler directory.

## Tests
To run all the python Tests at once run the "testall.py" file with 'python testall.py' in the WebCrawler directory.
Testclasses contains:
-   setUp
-   tearDown
-   The test functions with one Assertion each
-   Sample Data is from the file "GhExamples.py"
-   uses the built-in python unittests 

Following Code is from "GhAdapterTestsuite.py":
```
    def test_pos_get_all_attributes_with_everything1(self):
```
Functions start with "test" (unittests module requires it) then "pos" as a positive test.
"get_all_attributes" the actually function which is being tested and "with_everything1", info about the input data.
In this case has the input all necessary Info and because there are several like that, its uses the first variation of the that kind of data.
```        
        given_raw_site = self.__class__.TESTDATA_PRODDESC_WITH_PRODIMG_RAW_WITH_EVERYTHING1
        given_proddesc = get_proddesc_from_raw_site(given_raw_site)
        given_prodimg = get_prodimg_from_raw_site(given_raw_site)
```
Set the input for the upcoming function call.
```
        result_dict = GhAdapter.get_all_attributes(given_proddesc,given_prodimg)
```
Actually do the call.
```
        self.assertEqual(self.__class__.TESTDATA_DICT_WITH_EVERYTHING1,result_dict)
```
Assert.

## Contributers
If you want to join write me a message on Github.