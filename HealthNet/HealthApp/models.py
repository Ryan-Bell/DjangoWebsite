from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from abc import ABCMeta, abstractclassmethod
"""
The models.py is essentially where objects are declared. Currently, It holds the
PatientProfile object and the logItem object. These objects are most always referenced
in the views. In each class, fields are declared by giving the name followed by the type
of input field. Many of the models have a OneToOne link to another model. ManyToOne,
OneToMany, and ManyToMany are also other types of multiplicities allowed. These link the models.
"""

STATE_CHOICES = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
)

#This is used to limit the entry boxes
MAX_LENGTH = 50


class UserInfo(models.Model):
    policyNumber = models.CharField(max_length=MAX_LENGTH)
    provider = models.CharField(max_length=MAX_LENGTH)
    groupNumber = models.CharField(max_length=MAX_LENGTH)
    hospital = models.CharField(max_length=MAX_LENGTH, null=True)

class ProfileInfo(models.Model):
    firstName = models.CharField(max_length=MAX_LENGTH)
    middleName = models.CharField(blank=True, max_length=MAX_LENGTH)
    lastName = models.CharField(max_length=MAX_LENGTH)
    address = models.CharField(max_length=MAX_LENGTH)
    city = models.CharField(max_length=MAX_LENGTH, default='none')
    state = models.CharField(max_length=MAX_LENGTH, null=True)
    dateOfBirth = models.DateField(blank=True, null=True)
    zipcode = models.CharField(max_length=5)
    phoneNumber = models.CharField(max_length=14)
    email = models.EmailField(blank=False)
    eName = models.CharField(max_length=MAX_LENGTH, default='none')
    ePhoneNumber = models.CharField(max_length=MAX_LENGTH, default='none')

class MedicalInfo(models.Model):
    #add cancer
    #add diabetes
    allergies = models.BooleanField(default=False)
    anemia = models.BooleanField(default=False)
    arthritis = models.BooleanField(default=False)
    chickenpox = models.BooleanField(default=False)
    coxsackie = models.BooleanField(default=False)
    diphtheria = models.BooleanField(default=False)
    epilepsy = models.BooleanField(default=False)
    frequentColds = models.BooleanField(default=False)
    germanMeasles = models.BooleanField(default=False)
    highBloodPressure = models.BooleanField(default=False)
    influenza = models.BooleanField(default=False)
    kidneyDisease = models.BooleanField(default=False)
    measles = models.BooleanField(default=False)
    migraines = models.BooleanField(default=False)
    mumps = models.BooleanField(default=False)
    obesity = models.BooleanField(default=False)
    pneumonia = models.BooleanField(default=False)
    polio = models.BooleanField(default=False)
    rheumaticFever = models.BooleanField(default=False)
    scarlatina = models.BooleanField(default=False)
    scarletFever = models.BooleanField(default=False)
    strokes = models.BooleanField(default=False)
    syphilis = models.BooleanField(default=False)
    tonsillitis = models.BooleanField(default=False)
    tuberculosis = models.BooleanField(default=False)
    whoopingCough = models.BooleanField(default=False)
    otherText = models.CharField(max_length=MAX_LENGTH, null=True)

class Patient(models.Model):
    user = models.OneToOneField(User)
    userInfo = models.OneToOneField(UserInfo, null=True)
    profileInfo = models.OneToOneField(ProfileInfo, null=True)
    medicalInfo = models.OneToOneField(MedicalInfo, null=True)
    #prescriptions = models.ForeignKey(Prescription)
    #doctor = models.ForeignKey(Doctor)

    def __str__(self):
        return self.user.username

    #custom methods can be defined
    def getName(self):
        return self.userInfo.firstName + " " + self.userInfo.lastName

class Doctor(models.Model):
    user = models.OneToOneField(User)
    profileInfo = models.OneToOneField(ProfileInfo, null=True)


class Nurse(models.Model):
    user = models.OneToOneField(User)
    profileInfo = models.OneToOneField(ProfileInfo, null=True)





#class Logmanager? with many methods?
    #the logmanager would also keep track of the statistics
    #and viewing/sorting as well as making pretty graphs
    #methods for adding/retrieving logitems and sorting

#classes for the various tests that can be preformed with appropriate fields
#in addition, an accompaning form will need to be created
#all tests classes can inherit from a base test class that the patient will hold
#a list of

class LogItem(models.Model):
	user = models.OneToOneField(User)
	username = models.CharField(max_length=MAX_LENGTH)



"""

LEGACY CODE BELOW

class Doctor(models.Model):
    user = models.OneToOneField(User)
    profileInfo = models.OneToOneField(Profile, null=True)
    #Pertanint Methods here

class Nurse(models.Model):
    user = models.OneToOneField(User)
    profileInfo = models.OneToOneField(Profile, null=True)
    #Pertanint Methods here

class Admin(models.Model):
    user = models.OneToOneField(User)
    profileInfo = models.OneToOneField(Profile, null=True)
    #Pertanint Methods here

class Hospital(models.Model):
    name = models.CharField(max_length=MAX_LENGTH)
    address = models.CharField(max_length=MAX_LENGTH)
    city = models.CharField(max_length=MAX_LENGTH)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    zipcode = models.CharField(max_length=5)
'''
class Prescription:
    #medication
    medicationCategory = models.ForeignKey(choices=MEDICINE_CATEGORIES)
    medication = models.CharField(choices=medicationCategory.choices)
    #strength
    strength = models.CharField(choices=)
    #amount
    amount = models.CharField(choices=)
    #frequnecy
    frequency = models.CharField(choices=)
    #purpose (treatment for?)
    purpose = models.TextField()
    #directions
    directions = models.TextField()
    #comments
    comments = models.TextField()
'''

END LEGACY CODE

"""


#class for medication categories that each hold a list of medications
class Z_adamantane_antivirals(models.Model):
    SPECIFICS = (('amantadine', 'amantadine'),('rimantadine', 'rimantadine'))

class Z_adrenal_cortical_steroids(models.Model):
    SPECIFICS = (('corticotropin', 'corticotropin'), ('corticorelin', 'corticorelin'), ('cosyntropin', 'corsyntropin'),

                 ('triamcinolone', 'triamcinolone'), ('methylprednisolone', 'methylprednisolone'), ('betamethasone', 'betamethasone'),
                 ('prednisone', 'prednisone'), ('hydrocortisone', 'hydrocortisone'), ('budesonide', 'budesonide'),
                 ('prednisolone', 'prednisolone'), ('dexamethasone', 'dexamethasone'), ('cortisone', 'cortisone'),

                 ('fludrocortisone', 'fludrocortisone'))

class Z_adrenal_corticosteroid_inhibitors(models.Model):
    SPECIFICS = (('aminoglutethimide', 'aminoglutethimide'), ('metyrapone', 'metyrapone'))

class Z_adrenergic_bronchodilators(models.Model):
    SPECIFICS = (('isoproterenol', 'isoproterenol'), ('levalbuterol', 'levalbuterol'), ('arformoterol', 'arformoterol'),
                 ('epinephrine', 'epinephrine'), ('metaproterenol', 'metaproterenol'), ('terbutaline', 'terbutaline'),
                 ('formoterol', 'formoterol'), ('pirbuterol', 'pirbuterol'), ('racepinephrine', 'racepinephrine'), ('albuterol', 'albuterol'),
                 ('salmeterol', 'salmeterol'), ('bitolterol', 'bitolterol'), ('indacaterol', 'indacaterol'), ('isoetharine', 'isoetharine'), ('olodaterol', 'olodaterol'))

class Z_aldosterone_receptor_agents(models.Model):
    SPECIFICS = (('eplerenone', 'eplerenone'), ('spironolactone', 'spironolactone'))

class Z_alkylating_agents(models.Model):
    SPECIFICS = (('chlorambucil', 'chlorambucil'), ('bendamustine', 'bendamustine'), ('carboplatin', 'carboplatin'), ('cyclophosphamide', 'cyclophosphamide'), ('cisplatin', 'cisplatin'),
                 ('temozolomide', 'temozolomide'), ('busulfan', 'busulfan'), ('oxaliplatin', 'oxaliplatin'), ('melphalan', 'melphalan'), ('carmustine', 'carmustine'), ('dacarbazine', 'dacarbazine'),
                 ('isosfamide', 'isosfamide'), ('lomustine', 'lomustine'), ('mechlorethamine', 'mechlorethamine'), ('streptozocin', 'streptozocin'), ('thiotepa', 'thiotepa'))

class Z_alphaglucosidase_inhibitors(models.Model):
    SPECIFICS = (('miglitol', 'miglitol'), ('acarbose', 'acarbose'))

class Z_amebicides(models.Model):
    SPECIFICS = (('chloroquine', 'chloroquine'), ('nitazoxanide', 'nitazoxanide'), ('metronidazole', 'metronidazole'), ('tinidazole', 'tinidazole'), ('paromomycin', 'paromomycin'), ('iodoquinol', 'iodoquinol'))

class Z_aminoglycosides(models.Model):
    SPECIFICS = (('tobramycin', 'tobramycin'), ('paromomycin', 'paromomycin'), ('gentamicin', 'gentamicin'), ('amikacin', 'amikacin'),
                 ('kanamycin', 'kanamycin'), ('neomycin', 'neomycin'), ('streptomycin', 'streptomycin'))

class Z_aminopenicillins(models.Model):
    SPECIFICS = (('ampicillin', 'ampicillin'), ('amoxicillin', 'amoxicillin'), ('bacampicillin', 'bacampicillin'))

class Z_amylin_analogs(models.Model):
    SPECIFICS = (('pramlintide', 'pramlintide'))

class Z_analgesics(models.Model):
    SPECIFICS = (('methysergide', 'methysergide'), ('frovatriptan', 'frovatriptan'), ('naxproxen', 'naxproxen'), ('naratriptan', 'naratriptan'), ('almotriptan', 'almotriptan'), ('caffeine', 'caffeine'),
                 ('ergotamine', 'ergotamine'), ('rizatriptan', 'rizatriptan'), ('eletriptan', 'eletriptan'), ('acetaminophen', 'acetaminophen'), ('dichloralphenazone', 'dichloralphenazone'), ('isometheptene', 'isometheptene'),
                 ('sumatriptan', 'sumatriptan'), ('zolmitriptan', 'zolmaitriptan'), ('dihydroergotamine', 'dihydroergotamine'),

                 ('valdecoxib', 'valdecoxib'), ('rofecoxib', 'rofecoxib'), ('celecoxib', 'celecoxib'),

                 ('ziconotide', 'ziconotide'), ('levorphanol', 'levorphanol'), ('meperidine', 'meperidine'), ('butorphanol', 'butorphanol'), ('methadone', 'methadone'), ('hydromorphone', 'hydromorphone'),
                 ('oxycodone', 'oxycodone'), ('opium', 'opium'), ('fentanyl', 'fentanyl'), ('buprenorphine', 'buprenorphine'), ('oxymorphone', 'oxymorphone'), ('codeine', 'codeine'), ('morphine', 'morphine'),
                 ('nalbuphine', 'nalbuphine'), ('hydrocodone', 'hydrocodone'), ('propoxyphene', 'propoxyphene'), ('tramadol', 'tramadol'), ('tapentadol', 'tapentadol'), ('pentazocine', 'pentazoncine'), ('alfentanil', 'alfentanil'),
                 ('levomethadyl', 'levomethadyl'), ('remifentanil', 'remifentanil'), ('sufentanil', 'sufentanil'),

                 ('magnesium-salicylate', 'magnesium-salicylate'), ('aspirin', 'aspirin'), ('diflunisal','diflunisal'), ('salsalate', 'salsalate'))

class Z_anabolic_steroids(models.Model):
    SPECIFICS = (('methyltestosterone', 'methyltestosterone'), ('oxymetholone', 'oxymetholone'), ('testosterone', 'testosterone'), ('stanozolol', 'stanozolol'),
                 ('fluoxymesterone', 'fluoxymesterone'), ('nandrolone', 'nandrolone'), ('oxandrolone', 'oxandrolone'))

class Z_angiotensin_converting_enzyme_inhibitors(models.Model):
    SPECIFICS = (('captopril', 'captopril'), ('fosinopril', 'fosinopril'), ('moexipril', 'moexipril'), ('benazepril', 'benazepril'), ('ramipril', 'ramipril'), ('quinapril', 'quinapril'), ('enalapril', 'enalapril'),
                 ('perindopril', 'perindopril'), ('trandolapril', 'trandolapril'), ('lisinopril', 'lisinopril'))

class Z_anorexiants(models.Model):
    SPECIFICS = (('mazindol', 'mazindol'), ('diethylpropion', 'diethylpropion'), ('methamphetamine', 'methamphetamine'), ('phentermine', 'phentermine'), ('lorcaserin', 'lorcaserin'),('phendimetrazine', 'phendimetrazine'),
                 ('benzphetamine', 'benzphetamine'), ('sibutramine', 'sibutramine'), ('bupropion', 'bupropion'), ('phentermine', 'phentermine'))

class Z_anthelmintics(models.Model):
    SPECIFICS = (('albendazole', 'albendazole'), ('ivermectin', 'ivermectin'), ('praziquantel', 'praziquantel'), ('pyrantel', 'pyrantel'), ('mebendazole', 'mebendazole'), ('miltefosine', 'miltefosine'), ('niclosamide', 'niclosamide'),
                 ('oxamniquine', 'oxamniquine'), ('piperazine', 'piperazine'), ('thiabendazole', 'thiabendazole'))

class Z_antiandrogens(models.Model):
    SPECIFICS = (('bicalutamide', 'bicalutamide'), ('enzalutamide', 'enzalutamide'), ('flutamide', 'flutamide'), ('nilutamide', 'nilutamide'))

class Z_antianginal(models.Model):
    SPECIFICS = (('ranolazine', 'ranolazine'), ('nitroglycerin', 'nitroglycerin'), ('isosorbide-mononitrate', 'isosorbide-mononitrate'), ('isosorbide-dinitrate', 'isosorbide-dinitrate'), ('amyl-nitrite', 'amyl-nitrate'))

class Z_anticoagulants(models.Model):
    SPECIFICS = (('warfarin', 'warfarin'), ('fondaparinux', 'fondaparinux'), ('rivaroxban', 'rivaroxban'), ('apixaban', 'apixaban'), ('edoxaban', 'edoxaban'), ('dalteparin', 'dalteparin'), ('tinzaparin', 'tinzaparin'),
                 ('enoxaparin', 'enoxaparin'), ('heparin', 'heparin'), ('ardeparin', 'ardeparin'), ('danaparoid', 'danaparoid'),
                 ('bivalirudin', 'bivalirudin'), ('dabigatran', 'dabigatron'), ('argatroban', 'argatroban'), ('desirudin', 'desirudin'), ('lepirudin', 'lepirudin'))

class Z_anticonvulsants(models.Model):
    SPECIFICS = (('mephobarbital', 'mephobarbital'), ('primidone', 'primidone'), ('phenobarbital', 'phenobarbital'), ('clobazam', 'clobazam'), ('clonazepam', 'clonazepam'), ('diazepam', 'diazepam'), ('lorazepam', 'lorazepam'),
                 ('felbatol', 'felbatol'), ('acetazolamide', 'acetazolamide'), ('zonisamide', 'zonisamide'), ('topiramate', 'topiramate'), ('rufinamide', 'rufinamide'), ('oxcarbazepine', 'oxcarbazepine'), ('eslicrabazepinr', 'eslicarbazepine'),
                 ('carbamazepine', 'carbamazepine'), ('valproic-acid', 'valproic-acid'), ('divalproex-sodium', 'divalproex-sodium'), ('pregabalin', 'pregabalin'), ('vigabatrin', 'vigabatrin'), ('tiagabine', 'tiagabine'), ('phenytoin', 'phenytoin'),
                 ('ethotoin', 'ethotoin'), ('fosphenytoin', 'fosphenytoin'), ('mephenytoin', 'mephenytoin'), ('magnesium-sulfate', 'magnesium-sulfate'), ('lacosamide', 'lacosamide'), ('ezogabine', 'ezogabine'),
                 ('paramethadione', 'paramethadione'), ('trimethadione', 'trimethadione'), ('levetiracetam', 'levetiracetam'), ('ethosuximide', 'ethosuximide'), ('methsuximide', 'methsuximide'),
                 ('lamotrigine', 'lamotrigine'))


class Z_antidepressants(models.Model):
    SPECIFICS = (('bupropion', 'bupropion'), ('vilazodone', 'vilazodone'), ('vortioxetine', 'vortioxetine'), ('isocarboxazid', 'isocarboxazid'), ('tranycypromine', 'tranycypromine'), ('selegiline', 'selegiline'), ('phenelzine', 'phenelzine'),
                 ('nefazodone', 'nefazodone'), ('trazodone', 'trazodone'), ('escitalopram', 'excitalopram'), ('fluoxetine', 'fluoxetine'), ('citalopram', 'citalopram'), ('sertraline', 'sertraline'), ('paroxetine', 'paroxetine'), ('fluvoxamine', 'fluvoxamine'),
                 ('desvenlafaxine', 'desvenlafaxine'), ('venlafaxine', 'venlafaxine'), ('duloxetine', 'duloxetine'), ('milnacipran', 'milnacipran'), ('levomilnacipran', 'levomilnacipran'), ('maprotiline', 'maprotiline'), ('mirtazapine', 'mirtazapine'),
                 ('amoxapine', 'amoxapine'), ('desipramine', 'desipramine'), ('clomipramine', 'clomipramine'), ('trimipramine', 'trimipramine'), ('amitriptyline', 'amitriptyline'), ('nortriptyline', 'nortriptyline'), ('imipramine', 'imipramine'),('doxepin', 'doxepin'))


class Z_antidiabetic(models.Model):
    SPECIFICS = (('miglitol', 'miglitol'), ('acarbose', 'acarbose'), ('pramlintide', 'pramlintide'), ('liraglutide', 'liraglutide'), ('exenatide', 'exenatide'), ('dulaglutide', 'dulaglutide'), ('albiglutide', 'albiglutide'),
                 ('insulin', 'insulin'), ('repaglinide', 'repaglinide'), ('nateglinide', 'nateglinide'), ('chlorpropamide', 'chlorpropamide'), ('glimepiride', 'glimepiride'), ('glipizide', 'glipizide'), ('glyburide', 'glyburide'),
                 ('tolazamide', 'tolazamide'), ('acetohexamide', 'acetohexamide'), ('tolbutamide', 'tolbutamide'), ('rosiglitazone', 'roziglitazone'), ('pioglitazone', 'pioglitazone'), ('troglitazone', 'troglitazone'))

class Z_antidiarrheals(models.Model):
    SPECIFICS = (('atropine', 'atropine'), ('attapulgite', 'attapulgite'), ('saccharomyces-boulardii-lyo', 'saccharomyces-boulardii-lyo'), ('loperamide', 'loperamide'), ('bismuth-subsalicylate', 'bismuth-subsalicylate'), ('lactobacillius', 'lactobacillius'),
                 ('crofelemer', 'crofelemer'), ('kaolin', 'kaolin'), ('loperamide', 'loperamide'))


class Z_antidiuretics(models.Model):
    SPECIFICS = (('desmopressin', 'desmopressin'), ('vasopressin', 'vasopressin'))


class Z_antidotes(models.Model):
    SPECIFICS = (('prussian-blue', 'prussian-blue'), ('naloxone', 'naloxone'), ('pralidoxime', 'pralidoxime'), ('acetylcysteine', 'acetylcysteine'), ('naltrexone', 'naltrexone'), ('charcoal', 'charcoal'), ('atropine', 'atropine'),
                 ('deferiprone', 'deferiprone'), ('deferoxamine', 'deferoxamine'), ('digoxin', 'digoxin'), ('dimercaprol', 'dimercaprol'), ('edetate-calcium-disodium', 'edetate-calcium-disodium'), ('flumazenil', 'flumazenil'),
                 ('fomepizole', 'fomepizole'), ('glucarpidase', 'glucarpidase'), ('ipecac', 'ipecac'), ('leucovorin', 'leucovorin'), ('methylene-blue', 'methylene-blue'), ('nalmefene', 'nalmefene'), ('sodium-nirtate', 'sodium-nitrate'))


class Z_antifungals(models.Model):
    SPECIFICS = (('itraconazole', 'itroconazole'), ('posaconazole', 'posaconazole'), ('fluconazole', 'fluconazole'), ('ketoconazole', 'ketoconazole'), ('clotrimazole', 'clotrimazole'), ('isavuconazonium', 'isavuconazonium'), ('miconazole', 'miconazole'),
                 ('voriconazole', 'voriconazole'), ('anidulafungin', 'anidulafungin'), ('caspofungin', 'caspofungin'), ('micafungin', 'micafungin'), ('terbinafine', 'terbinafine'), ('griseofulvin', 'griseofulvin'), ('flucytosine', 'flucytosine'), ('hydroxypropyl-chitosan', 'hydroxypropyl-chitosan'))

class Z_antigonadotropic(models.Model):
    SPECIFICS = (('danazol', 'danazol'))


class Z_antigout(models.Model):
    SPECIFICS = (('probenecid','probenecid'), ('sulfinpyrazone', 'sulfinpyrazone'), ('allopurinol', 'allopurinol'), ('colchicine', 'colchicine'))


class Z_antihistamines(models.Model):
    SPECIFICS = (('dexchlorpheniramine', 'dexchlorpheniramine'), ('phenindamine', 'phenindamine'), ('terfenadine', 'terfenadine'), ('triprolidine', 'triprolidine'), ('carbinoxamine', 'carbinoxamine'), ('brompheniramine', 'brompheniramine'),
                 ('chlorpheniramine', 'chlorpheniramine'), ('cyproheptadine', 'cyproheptadine'), ('promethazine', 'promethazine'), ('levocetirizine', 'levocetirizine'), ('fexofenadine', 'fexofenadine'), ('clemastine', 'clemastine'), ('cetirizine', 'cetirizine'),
                 ('diphenhydramine', 'diphenhydramine'), ('desloratadine', 'desloratadine'), ('hydroxyzine', 'hydroxyzine'), ('loratadine', 'loratadine'), ('astemizole', 'astemizole'), ('azatadine', 'azatadine'), ('dexbrompheniramine', 'dexbrompheniramine'),
                 ('pheniramine', 'pheniramine'), ('pyrilamine', 'pyrilamine'), ('tripelennamine', 'tripelennamine'))


class Z_antimalarial(models.Model):
    SPECIFICS = (('chloroquine', 'chloroquine'), ('quinine', 'quinine'), ('hydroxychloroquine', 'hydroxychloroquine'), ('mefloquine', 'mefloquine'), ('primaquine', 'primaquine'), ('proguanil', 'proguanil'), ('doxycycline', 'doxycycline'), ('halofantrine', 'halofantrine'))


class Z_antimetabolites(models.Model):
    SPECIFICS = (('fluorouracil', 'fluorouracil'), ('cladribine', 'cladribine'), ('capecitabine', 'capecitabine'), ('methotrexate', 'methotrexate'), ('premetrexed', 'premetrexed'), ('mercaptopurine', 'mercaptopurine'), ('hydroxyurea', 'hydroxyurea'),
                 ('fludarabine', 'fludarabine'), ('gemcitabine', 'gemcitabine'), ('clofarabine', 'clofarabine'), ('cytarabine', 'cytarabine'), ('decitabine', 'decitabine'), ('floxuridine', 'floxuridine'), ('nelarabine', 'nelarabine'), ('pralatrexate', 'pralatrexate'))


class Z_anitmigraine(models.Model):
    SPECIFICS = (('methysergide', 'methysergide'), ('frovatriptan', 'frovatriptan'), ('naxproxen', 'naxproxen'), ('naratriptan', 'naratriptan'), ('almotriptan', 'almotriptan'), ('caffeine', 'caffeine'),
                 ('ergotamine', 'ergotamine'), ('rizatriptan', 'rizatriptan'), ('eletriptan', 'eletriptan'), ('acetaminophen', 'acetaminophen'), ('dichloralphenazone', 'dichloralphenazone'), ('isometheptene', 'isometheptene'),
                 ('sumatriptan', 'sumatriptan'), ('zolmitriptan', 'zolmaitriptan'), ('dihydroergotamine', 'dihydroergotamine'))

class Z_antiparkinson_agents(models.Model):
    SPECIFICS = (('benztropine', 'benztropine'), ('diphenhydramine', 'diphenhydramine'), ('trihexyphenidyl', 'trihexyphenidyl'), ('procyclidine', 'procyclidine'), ('biperiden', 'biperiden'))



class Z_antipsoriatics(models.Model):
    SPECIFICS = (('methotrexate', 'methotrexate'), ('acitretin', 'acitretin'))


class Z_antirheumatics(models.Model):
    SPECIFICS = (('auranofin', 'auranofin'), ('anakinra', 'anakinra'), ('infliximab', 'infliximab'), ('etanercept', 'etanercept'), ('rituximab', 'rituximab'), ('adalimumab', 'adalimumab'), ('penicillamine', 'penicillamine'), ('methotrexate', 'methotrexate'),
                 ('hyroxychloroquine', 'hydroxychloroquine'), ('tofacitinib', 'tofacitinib'), ('apremilast', 'apremilast'), ('leflunomide', 'leflunomide'), ('azathioprine', 'azathioprine'), ('abatacept', 'abatacept'), ('aurothioglucose', 'aurothioglucose'))


class Z_antiseptics(models.Model):
    SPECIFICS = (('hexachlorophene', 'hexachlorophene'), ('sodium-hypochlorite', 'sodium-hypochlorite'), ('chlorhexidine', 'chlorhexidine'), ('benalkonium', 'benalkonium'), ('iodine-topical', 'iodine-topical'), ('isopropanol', 'isopropanol'), ('povidone-iodine', 'povidone-iodine'))


class Z_antithyroid(models.Model):
    SPECIFICS = (('potassium-iodide', 'potassium-iodide'), ('propylthiouracil', 'propylthiouracil'), ('methimazole', 'methimazole'))


class Z_barbiturates(models.Model):
    SPECIFICS = (('secobarbital', 'secobarbital'), ('mephobarbital', 'mephobarbital'), ('pentobarbital', 'pentobarbital'), ('phenobarbital', 'phenobarbital'), ('butabarbital', 'butabarbital'), ('amobarbital', 'amobarbital'))


class Z_benzodiazepines(models.Model):
    SPECIFICS = (('quazepam', 'quazepam'), ('estazolam', 'estazolam'), ('clobazam', 'clobazam'), ('alphrazolam', 'alphrazolam'), ('flurazepam', 'flurazepam'), ('oxazepam', 'oxazepam'), ('chlordiazepoxide', 'chlordiazepoxide'), ('clonazepam', 'cloneazapam'),
                 ('diazepam', 'diazepam'), ('lorazepam', 'lorazepam'), ('clorazepate', 'clorazepate'), ('triazolam', 'triazolam'), ('midazolam', 'midazolam'), ('temazepam', 'temazepam'), ('halazepam', 'halazepam'))


class Z_bisphosphonates(models.Model):
    SPECIFICS = (('alendronate', 'alendronate'), ('etidronate', 'etidronate'), ('zoledronic-acid', 'zoledronic-acid'), ('ibandronate', 'ibandronate'), ('alendronate', 'alendronate'), ('risedronate', 'risedronate'), ('pamidronate', 'pamidronate'), ('tiludronate', 'tiludronate'))


class Z_calcineurin_inhibitors(models.Model):
    SPECIFICS = (('cyclosporine', 'cyclosporine'), ('tacrolimus', 'tacrolimus'))


class Z_calcitonin(models.Model):
    SPECIFICS = (('calcitonin', 'calcitonin'))


class Z_carbapenems(models.Model):
    SPECIFICS = (('doripenem', 'doripenem'), ('meropenem', 'meropenem'), ('cilastatin', 'cilastatin'), ('ertapenem', 'ertapenem'))


class Z_cardiac_stressing_agents(models.Model):
    SPECIFICS = (('adenosine', 'adenosine'), ('regadensoson', 'regadensoson'), ('dobutamine', 'dobutamine'), ('dipyridamole', 'dipyridamole'))


class Z_catecholamines(models.Model):
    SPECIFICS = (('isoproterenol', 'isoproterenol'), ('epinephrine', 'epinephrine'), ('norepinephrine', 'norepinephrine'), ('dobutamine', 'dobutamine'), ('dopamine', 'dopamine'))


class Z_cerumenolytics(models.Model):
    SPECIFICS = (('carbamide-peroxide', 'carbamide-peroxide'), ('trithanolamine-polypeptide-oleate', 'trithanolamine-polypeptide-oleate'))


class Z_chelating_agents(models.Model):
    SPECIFICS = (('deferasirox', 'deferasirox'), ('deferiprone', 'deferiprone'), ('deferoxamine', 'deferoxamine'), ('succimer', 'succimer'), ('trientine', 'trientine'))


class Z_cholinergic_muscle_stimulants(models.Model):
    SPECIFICS = (('dalfampridine', 'dalfampridine'), ('neostigmine', 'neostigmine'), ('pyridostigmine', 'pyridostigmine'), ('ambenonium', 'ambenonium'), ('atropine', 'atropine'), ('edrophonium', 'edrophonium'), ('guanidine', 'guanidine'))


class Z_cholinesterase_inhibitors(models.Model):
    SPECIFICS = (('tacrine', 'tacrine'), ('galantamine', 'galantamine'), ('rivastigmine', 'rivastigmine'), ('donepezil', 'donepezil'))


class Z_contraceptives(models.Model):
    SPECIFICS = (('ethinyl-estradiol', 'ethinyl-estradiol'), ('levonorgestrel', 'levonorgestrel'), ('dienogest', 'dienogest'), ('mestranol', 'mestranol'), ('drospirenone', 'drospirenone'), ('desogestrel', 'desogestrel'))


class Z_decongestants(models.Model):
    SPECIFICS = (('phenylpropanolamine', 'phenylpropanolamine'), ('pseudoephedrine', 'pseudoephedrine'), ('ephedrine', 'ephedrine'), ('phenylephrine', 'phenylephrine'))


class Z_digestive_enzymes(models.Model):
    SPECIFICS = (('pancrelipase', 'pancrelipase'), ('pancreatin', 'pancreatin'), ('lactase', 'lactase'), ('amylase', 'amylase'), ('cholic-acid', 'cholic-acid'), ('sacrosidase', 'sacrosidase'))


class Z_echinocandins(models.Model):
    SPECIFICS = (('caspofungin', 'caspofungin'), ('anidulafungin', 'anidulafungin'), ('micfungin', 'micafungin'))


class Z_estrogens(models.Model):
    SPECIFICS = (('estropipate', 'estropipate'), ('esterified', 'esterified'), ('estadiol', 'estradiol'), ('chlorotrianisene', 'chlorotrianisene'))


class Z_expectorants(models.Model):
    SPECIFICS = (('potassium-iodide', 'potassium-iodide'), ('guaifenesin', 'guaifenesin'), ('carbocysteine', 'carbocysteine'), ('potassium-guaiacolsulfonate', 'potassium-guaiacolsulfonate'))


class Z_fibric_acid_derivatives(models.Model):
    SPECIFICS = (('gemfibrozil', 'gemfibrozil'), ('fenofibrate', 'fenofibrate'), ('clofibrate', 'clofibrate'))


class Z_gallstone_solubilizing_agents(models.Model):
    SPECIFICS = (('ursodiol', 'ursodiol'), ('chenodeoxycholic-acid', 'chenodeoxycholic-acid'), ('monoctanoin', 'monoctanoin'))


class Z_general_anesthetics(models.Model):
    SPECIFICS = (('propofol', 'propofol'), ('thiopental', 'thiopental'), ('ketamine', 'ketamine'), ('desflurane', 'desflurane'), ('droperidol', 'droperidol'), ('enflurane', 'enflurane'), ('etomidate', 'etomidate'), ('fospropofol', 'forpropofol'), ('halothane', 'halothane'),
                 ('isoflurane', 'isoflurane'), ('methohexital', 'methohexital'), ('nitrous-oxide', 'nitrous-oxide'), ('sevoflurane', 'sevoflurane'))


class Z_gi_stimulants(models.Model):
    SPECIFICS = (('metoclopramide', 'metoclopramide'), ('cisapride', 'cisapride'), ('choline-bitartrate', 'choline-bitartrate'))


class Z_growth_hormones(models.Model):
    SPECIFICS = (('somatropin', 'somatropin'), ('tesamorelin', 'tesamorelin'), ('serorelin', 'sermorelin'))


class Z_impotence_agents(models.Model):
    SPECIFICS = (('tadalafil', 'tadalafil'), ('sildenafil', 'sildenafil'), ('vardenafil', 'vardenafil'), ('alprostadil', 'alprostadil'), ('avanafil', 'avanafil'), ('yohimbine', 'yohimbine'))


class Z_inhaled_antiinfectives(models.Model):
    SPECIFICS = (('tobramycin', 'tobramycin'), ('zanamivir', 'zanamivir'), ('ribavirin', 'ribavirin'), ('pentamidine', 'pentamidine'))


class Z_inhaled_corticosteroids(models.Model):
    SPECIFICS = (('flunisolide', 'flunisolide'), ('fluticasone', 'fluticasone'), ('ciclesonide', 'ciclesonide'), ('beclomethasone', 'beclomethasone'), ('budesonide', 'budesonide'), ('mometasone', 'mometasone'))


class Z_inotropic_agents(models.Model):
    SPECIFICS = (('digoxin', 'digoxin'), ('dobutamine', 'dobutamine'), ('dopamine', 'dopamine'), ('inamrinone', 'inamrinone'), ('milrinone', 'milrinone'))


class Z_interleukins(models.Model):
    SPECIFICS = (('proleukin', 'proleukin'), ('neumega', 'neumega'))


class Z_ketolides(models.Model):
    SPECIFICS = (('telithromycin', 'telithromycin'))


class Z_laxatives(models.Model):
    SPECIFICS = (('magnesium-citrate', 'magnesium-citrate'), ('lactulose', 'lactulose'), ('cascara-sagrada', 'cascara-sagrada'), ('polycarbophil', 'polycarbophil'), ('magnesium-hydroxide', 'magnesium-hydroxide'),
                 ('glycerin', 'glycerin'), ('polyethylene-glycol-3350', 'polythylene-glycol-3350'), ('sodium-biphosphate', 'sodium-biphosphate'), ('docusate', 'docusate'), ('psyllium', 'psyllium'),
                 ('magnesium-sulfate', 'magnesium-sulfate'), ('methylcellulose', 'methylcellulose'), ('docusate', 'docusate'), ('bisacodyl', 'bisacodyl'), ('senna', 'senna'), ('castor-oil', 'castor-oil'),
                 ('guar-gum', 'guar-gum'), ('hydrocortisone', 'hydrocortisone'), ('inulin', 'inulin'), ('magnesium-sulfate', 'magnesium-sulfate'), ('mineral-oil', 'mineral-oil'), ('sorbitol', 'sorbitol'))

class Z_leprostatics(models.Model):
    SPECIFICS = (('clofazimine', 'clofazimine'), ('thalidomide', 'thalidomide'))


class Z_lincomycin_derivatives(models.Model):
    SPECIFICS = (('lincomycin', 'lincomycin'), ('clindamycin', 'clindamycin'))


class Z_loop_diuretics(models.Model):
    SPECIFICS = (('bumetanide', 'bumetanide'), ('ethacrynic-acid', 'ethacrynic-acid'), ('furosemide', 'furosemide'), ('torsemide', 'torsemide'))


class Z_lung_surfactants(models.Model):
    SPECIFICS = (('poractant', 'poractant'), ('lucinactant', 'lucinactant'), ('beractant', 'beractant'), ('calfactant', 'calfactant'))


class Z_lysosomal_enzymes(models.Model):
    SPECIFICS = (('imiglucerase', 'imiglucerase'), ('alglucosidase', 'alglucosidase'), ('alglucerase', 'alglucerase'), ('elosulfase', 'elosulfase'), ('galsulfase', 'galsulfase'), ('idursulfase', 'idursulfase'), ('laronidase', 'laronidase'),
                 ('taliglucerase', 'taliglucerase'), ('velaglucerase', 'velaglucerase'))


class Z_macrolides(models.Model):
    SPECIFICS = (('dirithromycin', 'dirithromycin'), ('fidaxomicin', 'fidazomicin'), ('azithromycin', 'azithromycin'), ('clarithromycin', 'clarithromycin'), ('erythromycin', 'erythromycin'), ('troleandomycin', 'troleandomycin'))


class Z_methylxanthines(models.Model):
    SPECIFICS = (('oxtriphylline', 'oxtriphylline'), ('theophylline', 'theophylline'), ('aminophylline', 'aminophylline'), ('dyphylline', 'dyphylline'))


class Z_mitotic_inhibitors(models.Model):
    SPECIFICS = (('eribulin', 'eribulin'), ('paclitaxel', 'paclitaxel'), ('vincristine', 'vincristine'), ('paclitaxel', 'paclitaxel'), ('etoposide', 'etoposide'), ('docetaxel', 'docetaxel'), ('cabazitaxel', 'cabazitazel'), ('estramustine', 'estramustine'),
                 ('ixabepilone', 'ixabepilone'), ('teniposide', 'teniposide'), (' vinblastine', 'vinblastine'), ('vincristine', 'vincristine'), ('vinorelbine', 'vinorelbine'))


class Z_mydriatics(models.Model):
    SPECIFICS = (('cyclopentolate', 'cyclopentolate'), ('tropicamide', 'tropicamide'), ('atropine', 'atropine'), ('homatropine', 'homatropine'), ('hydroxyamphetamine', 'hydroxyamphetamine'), ('phenylephrine', 'phenylephrine'), ('scopolamine', 'scopolamine'))


class Z_nasal_steroids(models.Model):
    SPECIFICS = (('flunisolide', 'flunisolide'), ('budesonide', 'budesonide'), ('beclomehtasone', 'beclomethasone'), ('ciclesonide', 'ciclesonide'), ('mometasone', 'mometasone'), ('azelastine', 'azelastine'), ('fluticasone', 'fluticasone'), ('triamcinolone', 'triamcinolone'))


class Z_phosphate_binders(models.Model):
    SPECIFICS = (('sucroferric-oxyhydroxide', 'sucroferric-oxyhydroxide'), ('sevelamer', 'sevelamer'), ('aluminum-hydroxide', 'aluminum-hydroxide'), ('lanthanum-carbonate', 'lanthanum-carbonate'), ('calcium-acetate', 'calcium-acetate'), ('ferric-citrate', 'ferric-citrate'))


class Z_probiotics(models.Model):
    SPECIFICS = (('saccharomyces-boulardii-lyo', 'saccharomyces-boulardii-lyo'), ('bifidobacterium-infantis', 'bifidobacterium-infantis'), ('lactobacillus', 'lactobacillus'))


class Z_progestins(models.Model):
    SPECIFICS = (('hydroxyprogesterone', 'hydroxyprogesterone'), ('megestrol', 'megestrol'), ('levonorgestrel', 'levonorgestrel'), ('progesterone', 'progesterone'), ('etonogestrel','etonogestrel'), ('norethindrone', 'norethindrone'))


class Z_purine_nucleosides(models.Model):
    SPECIFICS = (('ganciclovir', 'ganciclovir'), ('valacyclovir', 'valacyclovir'), ('famciclovir', 'famciclovir'), ('acyclovir', 'acyclovir'), ('ribavirin', 'ribavirin'), ('cidofovir', 'cidofovir'), ('valganciclovir', 'valganciclovir'))


class Z_quinolones(models.Model):
    SPECIFICS = (('lomefloxacin', 'lomefloxacin'), ('norfloxacin', 'norfloxacin'), ('ofloxacin', 'ofloxacin'), ('gatifloxacin', 'gatifloxacin'), ('moxifloxacin', 'moxifloxacin'), ('ciprofloxacin', 'ciprofloxacin'), ('levofloxacin', 'levofloxacin'),
                 ('gemifloxacin', 'gemifloxacin'), ('cinoxacin', 'cinoxacin'), ('enoxacin', 'enoxacin'), ('grepafloxacin', 'grepafloxacin'), ('nalidixic', 'nalidixic'), ('sparfloxacin', 'sparfloxacin'), ('trovafloxacin', 'trovafloxacin'))


class Z_sclerosing_agents(models.Model):
    SPECIFICS = (('ethanolamine-oleate', 'ethanolamine-oleate'), ('morrhuate', 'morrhuate'), ('polidocanol', 'polidocanol'), ('sodium-tetradecyl-sulfate', 'sodium-tetradecyl-sulfate'))


class Z_thrombolytics(models.Model):
    SPECIFICS = (('alteplase', 'alteplase'), ('streptokinase', 'streptokinase'), ('reteplase', 'reteplase'), ('tenecteplase', 'tenecteplase'), ('urokinase', 'urokinase'))


class Z_uterotonic_agents(models.Model):
    SPECIFICS = (('carboprost', 'carboprost'), ('mifepristone', 'mifepristone'), ('methylergonovine', 'methylergonovine'), ('oxytocin', 'oxytocin'), ('dinoprostone', 'dinoprostone'), ('ergonovine', 'ergonovine'))


class Z_vasodilators(models.Model):
    SPECIFICS = (('nitroglycerin', 'nitroglycerin'), ('alprostadil', 'alprostadil'), ('hydralazine', 'hydralazine'), ('minoxidil', 'minoxidil'), ('nesiritide', 'nesiritide'), ('nitroprusside', 'nitroprusside'), ('riociguat', 'riociguat'))



MEDICINE_CATEGORIES = (('adrenal_cortical_steroids', Z_adrenal_cortical_steroids),
                       ('adrenal_corticosteroid_inhibitors', Z_adrenal_corticosteroid_inhibitors),
                       ('adrenergic_bronchodilators', Z_adrenergic_bronchodilators),
                       ('aldosterone_receptor_agents', Z_aldosterone_receptor_agents),
                       ('alkylating_agents', Z_alkylating_agents),
                       ('alphaglucosidase_inhibitors', Z_alphaglucosidase_inhibitors),
                       ('amebicides', Z_amebicides),
                       ('aminoglycosides', Z_aminoglycosides),
                       ('aminopenicillins', Z_aminopenicillins),
                       ('amylin_analogs', Z_amylin_analogs),
                       ('analgesics', Z_analgesics),
                       ('anabolic_steroids', Z_anabolic_steroids),
                       ('angiotensin_converting_enzyme_inhibitors', Z_angiotensin_converting_enzyme_inhibitors),
                       ('anorexiants', Z_anorexiants),
                       ('anthelmintics', Z_anthelmintics),
                       ('antiandrogens', Z_antiandrogens),
                       ('antianginal', Z_antianginal),
                       ('anticoagulants', Z_anticoagulants),
                       ('anticonvulsants', Z_anticonvulsants),
                       ('antidepressants', Z_antidepressants),
                       ('antidiabetic', Z_antidiabetic),
                       ('antidiarrheals', Z_antidiarrheals),
                       ('antidiuretics', Z_antidiuretics),
                       ('antidotes', Z_antidotes),
                       ('antifungals', Z_antifungals),
                       ('antigonadotropic', Z_antigonadotropic),
                       ('antigout', Z_antigout),
                       ('antihistamines', Z_antihistamines),
                       ('antimalarial', Z_antimalarial),
                       ('antimetabolites', Z_antimetabolites),
                       ('anitmigraine', Z_anitmigraine),
                       ('antiparkinson_agents', Z_antiparkinson_agents),
                       ('antipsoriatics', Z_antipsoriatics),
                       ('antirheumatics', Z_antirheumatics),
                       ('antiseptics', Z_antiseptics),
                       ('antithyroid', Z_antithyroid),
                       ('barbiturates', Z_barbiturates),
                       ('benzodiazepines', Z_benzodiazepines),
                       ('bisphosphonates', Z_bisphosphonates),
                       ('calcineurin_inhibitors', Z_calcineurin_inhibitors),
                       ('calcitonin', Z_calcitonin),
                       ('carbapenems', Z_carbapenems),
                       ('cardiac_stressing_agents', Z_cardiac_stressing_agents),
                       ('catecholamines', Z_catecholamines),
                       ('cerumenolytics', Z_cerumenolytics),
                       ('chelating_agents', Z_chelating_agents),
                       ('cholinergic_muscle_stimulants', Z_cholinergic_muscle_stimulants),
                       ('cholinesterase_inhibitors', Z_cholinesterase_inhibitors),
                       ('contraceptives', Z_contraceptives),
                       ('decongestants', Z_decongestants),
                       ('digestive_enzymes', Z_digestive_enzymes),
                       ('echinocandins', Z_echinocandins),
                       ('estrogens', Z_estrogens),
                       ('expectorants', Z_expectorants),
                       ('fibric_acid_derivatives', Z_fibric_acid_derivatives),
                       ('gallstone_solubilizing_agents', Z_gallstone_solubilizing_agents),
                       ('general_anesthetics', Z_general_anesthetics),
                       ('gi_stimulants', Z_gi_stimulants),
                       ('growth_hormones', Z_growth_hormones),
                       ('impotence_agents', Z_impotence_agents),
                       ('inhaled_antiinfectives', Z_inhaled_antiinfectives),
                       ('inhaled_corticosteroids', Z_inhaled_corticosteroids),
                       ('inotropic_agents', Z_inotropic_agents),
                       ('interleukins', Z_interleukins),
                       ('ketolides', Z_ketolides),
                       ('laxatives', Z_laxatives),
                       ('leprostatics', Z_leprostatics),
                       ('lincomycin_derivatives', Z_lincomycin_derivatives),
                       ('loop_diuretics', Z_loop_diuretics),
                       ('lung_surfactants', Z_lung_surfactants),
                       ('lysosomal_enzymes', Z_lysosomal_enzymes),
                       ('macrolides', Z_macrolides),
                       ('methylxanthines', Z_methylxanthines),
                       ('mitotic_inhibitors', Z_mitotic_inhibitors),
                       ('mydriatics', Z_mydriatics),
                       ('nasal_steroids', Z_nasal_steroids),
                       ('phosphate_binders', Z_phosphate_binders),
                       ('probiotics', Z_probiotics),
                       ('progestins', Z_progestins),
                       ('purine_nucleosides', Z_purine_nucleosides),
                       ('quinolones', Z_quinolones),
                       ('sclerosing_agents', Z_sclerosing_agents),
                       ('thrombolytics', Z_thrombolytics),
                       ('uterotonic_agents', Z_uterotonic_agents),
                       ('vasodilators', Z_vasodilators))

