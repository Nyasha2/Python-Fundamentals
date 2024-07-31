import random
import pytest
import string

import sys

sys.path.insert(0, '../lab03_files')
from lab03 import decode_skip_code


# def generate_test_files():
#    input = open("lab03_files/tests/dictionary.txt", "r")
#    text = input.read()
#    words = text.split("\n")
    
#    for i in range(20):
#       output = open(f"lab03_files/tests/test_files_03/test_file{i}.txt", "w")
      
#       output_string = ""
#       for _ in range(250):
#          # random_index = random.randint(0, len(text) - 1)
#          # output_string += text[random_index] + " "
#          output_string += random.choice(words) + " "
      
#       output.write(output_string)
    
#    input.close()
#    output.close()

# def generate_test_answers():
#    for i in range(20):
#       filepath = f"lab03_files/tests/test_files_03/test_file{i}.txt"
#       input = open(filepath, "r")
#       text = input.read()
#       words = text.split()

#       start_word = random.choice(words)
#       skip_amount = random.randint(1, 10)

#       print(i)
#       print(start_word)
#       print(skip_amount)
#       print(decode_skip_code(filepath, start_word, skip_amount))
#       print()

#       input.close()
# def test_decode_skip_code_divide_by_zero_error():
#    with pytest.raises(Exception):
#       decode_skip_code("tests/test_files_03/test_file0.txt", 0)

def cleaned(path, skip):
   return decode_skip_code(path, skip).strip()

def test_decode_skip_code_no_start_code():
   assert cleaned("tests/test_files_03/test_file0.txt", 1) == \
      "immunised physitheistic chlorpicrin broughta werwolf gulches tautochronous submanor vaticinate abditive danian unslow parcel petalodontoid procumbent immunised absolutization corniche euryscope florification prehesitate superoctave keraunophonic pullulate archcorrupter exophoria discubitory watchmanly unbottled meagre coracoprocoracoid nonpriestly tuberculosectorial lutjanidae amberjacks maritally xylotomic vagabondish thyrotropin biter malpais mastiffs macaronically unsailable vassalless demonstratively diestocks dragonnade troupials strabometry stepless flawlessly ambarella overneutralizer geometrize sokemen imitant prosonomasia unconfutability chromoleucite gestura gayals untriumphantly orthotone unexactingness raymond precherish apocryphalness unspiritualising purlins jelick astroite rascals meteor cowson outhammer investitures preexhibit pictorialisation insolence acroterion accruement tetracolon relucent fecifork foulnesses rhyolitic wombstone unifoliolate pococurantism overbeetling estampede anticatalase esterified nummuline noncongruous studiousness ericeticolous unarrogated crapulously philippan heliodor homoeoarchy gaped uncocked linsangs machrees cudbear homaloptera epacme percolator olaf hassenpfeffer mesole hypnagogic ameen ahong protogyny easters wotting boondoggler directionally laevogyrate amate squeaks gratuities bequeath unshackled washstands homeopolar obiisms ammonoid"

def test_decode_skip_code():
   assert cleaned("tests/test_files_03/test_file0.txt", 9) \
      == "vaticinate corniche discubitory maritally vassalless overneutralizer untriumphantly astroite acroterion pococurantism unarrogated cudbear ahong gratuities"

def test_decode_skip_code2():
   assert cleaned("tests/test_files_03/test_file1.txt", 7) \
      == "supertartrate palsgraf hyloist frayproof cliffier peramelidae charabancs braireau sludge sapin"

def test_decode_skip_code3():
   assert cleaned("tests/test_files_03/test_file2.txt", 9) \
      == "linin mistakenness hoopla halidome remancipation"

def test_decode_skip_code4():
   assert cleaned("tests/test_files_03/test_file3.txt", 5) \
      == "humoring epiderms tziganes synergically fabricate fetishism procreative"

def test_decode_skip_code5():
   assert cleaned("tests/test_files_03/test_file4.txt", 7) \
      == "trichostrongylid stabilizing innermostly hypate widely douched intransigency fairlike chromatopathy jazyges troughing future hymenocallis flowstone sectility"

def test_decode_skip_code6():
   assert cleaned("tests/test_files_03/test_file5.txt", 9) \
      == "refine dendroid micrencephalic undiscriminative craquelures violentness annihilability mayoralty orthotomous overgoads remeasured aduncous insubmergible colombians liernes sturiones sitfast enwomb ethnogeographer"

def test_decode_skip_code7():
   assert cleaned("tests/test_files_03/test_file6.txt", 9) \
      == "hellions overbar methodiser viewing shinnying pepysian albicores outchidden dipstick ivorine puzzleheadedly smooches"

def test_decode_skip_code8():
   assert cleaned("tests/test_files_03/test_file7.txt", 2) \
      == "combattant helminthagogue sulfonmethane condylura oneiromancy oligomerous scuppered coadjuvant larrigans unresistingness microorganism advoyer uncreaturely renouncement boppers amphibion mylonites gaullist hays desegmentation potamonidae hype asklepios resimmer asperifoliae toolbuilding infinitation hormogonales cruised obtrude buckhorn gaddis sidesmen acineta iglulirmiut gargalize ecclesiasticus zibethone downcomes conformably schorls acceptavit interpalpebral asseverate debitor elenchize bilateralities contineu pascal saul enfeoffing spunkie ghettoizes distensile pearmonger hepatitis subgoals overinventoried prededicated fendillation mingledly tussling ectogenesis superattainably hitchhiking grievances floors typhization unfragrance betides conf accounsel hierurgies jelly profitlessness lyricists roundel nonperceptibly scolecology kaama gulonic overshadows morbiferous viziercraft libelists radidii skatole unremember extendable phytotron takilman unsinewed windhover bagnios countrieman zairians unfeared madril calfdozer garnetberry"

def test_decode_skip_code9():
   assert cleaned("tests/test_files_03/test_file8.txt", 10) \
      == "svarajs arendalite metalorganic unrestraint ragusye interrelations goup thrustle subcompleteness shamal conqueringly killikinic"