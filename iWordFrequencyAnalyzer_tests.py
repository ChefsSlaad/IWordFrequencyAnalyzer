import unittest

import iWordFrequencyAnalyzer


class WordFrequencyAnalyzer_tests(unittest.TestCase):
    def setUp(self):
        self.analyzer = iWordFrequencyAnalyzer.iWordFrequencyAnalyzer()

        self.in_1 = r"The sun shines over the lake"
        self.in_2 = r"""
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                    sed do eiusmod tempor incididunt ut labore et dolore magna
                    aliqua. Ut enim ad minim veniam, quis nostrud exercitation
                    ullamco laboris nisi ut aliquip ex ea commodo consequat.
                    Duis aute irure dolor in reprehenderit in voluptate velit
                    esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
                    occaecat cupidatat non proident, sunt in culpa qui officia
                    deserunt mollit anim id est laborum."
                    """
        self.in_3 = r"""
                    Once upon a midnight dreary, while I pondered, weak and weary,
                    Over many a quaint and curious volume of forgotten lore-
                        While I nodded, nearly napping, suddenly there came a tapping,
                    As of some one gently rapping, rapping at my chamber door.
                    "'Tis some visitor," I muttered, "tapping at my chamber door-
                                Only this and nothing more."

                        Ah, distinctly I remember it was in the bleak December;
                    And each separate dying ember wrought its ghost upon the floor.
                        Eagerly I wished the morrow;-vainly I had sought to borrow
                        From my books surcease of sorrow-sorrow for the lost Lenore-
                    For the rare and radiant maiden whom the angels name Lenore-
                                Nameless here for evermore.

                        And the silken, sad, uncertain rustling of each purple curtain
                    Thrilled me-filled me with fantastic terrors never felt before;
                        So that now, to still the beating of my heart, I stood repeating
                        "'Tis some visitor entreating entrance at my chamber door-
                    Some late visitor entreating entrance at my chamber door;-
                                This it is and nothing more."

                        Presently my soul grew stronger; hesitating then no longer,
                    "Sir," said I, "or Madam, truly your forgiveness I implore;
                        But the fact is I was napping, and so gently you came rapping,
                        And so faintly you came tapping, tapping at my chamber door,
                    That I scarce was sure I heard you"-here I opened wide the door;-
                                Darkness there and nothing more.

                        Deep into that darkness peering, long I stood there wondering, fearing,
                    Doubting, dreaming dreams no mortal ever dared to dream before;
                        But the silence was unbroken, and the stillness gave no token,
                        And the only word there spoken was the whispered word, "Lenore?"
                    This I whispered, and an echo murmured back the word, "Lenore!"-
                                Merely this and nothing more.

                        Back into the chamber turning, all my soul within me burning,
                    Soon again I heard a tapping somewhat louder than before.
                        "Surely," said I, "surely that is something at my window lattice;
                          Let me see, then, what thereat is, and this mystery explore-
                    Let my heart be still a moment and this mystery explore;-
                                'Tis the wind and nothing more!"

                        Open here I flung the shutter, when, with many a flirt and flutter,
                    In there stepped a stately Raven of the saintly days of yore;
                        Not the least obeisance made he; not a minute stopped or stayed he;
                        But, with mien of lord or lady, perched above my chamber door-
                    Perched upon a bust of Pallas just above my chamber door-
                                Perched, and sat, and nothing more.

                    Then this ebony bird beguiling my sad fancy into smiling,
                    By the grave and stern decorum of the countenance it wore,
                    "Though thy crest be shorn and shaven, thou," I said, "art sure no craven,
                    Ghastly grim and ancient Raven wandering from the Nightly shore-
                    Tell me what thy lordly name is on the Night's Plutonian shore!"
                                Quoth the Raven "Nevermore."

                        Much I marvelled this ungainly fowl to hear discourse so plainly,
                    Though its answer little meaning-little relevancy bore;
                        For we cannot help agreeing that no living human being
                        Ever yet was blessed with seeing bird above his chamber door-
                    Bird or beast upon the sculptured bust above his chamber door,
                                With such name as "Nevermore."

                        But the Raven, sitting lonely on the placid bust, spoke only
                    That one word, as if his soul in that one word he did outpour.
                        Nothing farther then he uttered-not a feather then he fluttered-
                        Till I scarcely more than muttered "Other friends have flown before-
                    On the morrow he will leave me, as my Hopes have flown before."
                                Then the bird said "Nevermore."

                        Startled at the stillness broken by reply so aptly spoken,
                    "Doubtless," said I, "what it utters is its only stock and store
                        Caught from some unhappy master whom unmerciful Disaster
                        Followed fast and followed faster till his songs one burden bore-
                    Till the dirges of his Hope that melancholy burden bore
                                Of 'Never-nevermore'."

                        But the Raven still beguiling all my fancy into smiling,
                    Straight I wheeled a cushioned seat in front of bird, and bust and door;
                        Then, upon the velvet sinking, I betook myself to linking
                        Fancy unto fancy, thinking what this ominous bird of yore-
                    What this grim, ungainly, ghastly, gaunt, and ominous bird of yore
                                Meant in croaking "Nevermore."

                        This I sat engaged in guessing, but no syllable expressing
                    To the fowl whose fiery eyes now burned into my bosom's core;
                        This and more I sat divining, with my head at ease reclining
                        On the cushion's velvet lining that the lamp-light gloated o'er,
                    But whose velvet-violet lining with the lamp-light gloating o'er,
                                She shall press, ah, nevermore!

                        Then, methought, the air grew denser, perfumed from an unseen censer
                    Swung by Seraphim whose foot-falls tinkled on the tufted floor.
                        "Wretch," I cried, "thy God hath lent thee-by these angels he hath sent thee
                        Respite-respite and nepenthe from thy memories of Lenore;
                    Quaff, oh quaff this kind nepenthe and forget this lost Lenore!"
                                Quoth the Raven "Nevermore."

                        "Prophet!" said I, "thing of evil!-prophet still, if bird or devil!-
                    Whether Tempter sent, or whether tempest tossed thee here ashore,
                        Desolate yet all undaunted, on this desert land enchanted-
                        On this home by Horror haunted-tell me truly, I implore-
                    Is there-is there balm in Gilead?-tell me-tell me, I implore!"
                                Quoth the Raven "Nevermore."

                        "Prophet!" said I, "thing of evil!-prophet still, if bird or devil!
                    By that Heaven that bends above us-by that God we both adore-
                        Tell this soul with sorrow laden if, within the distant Aidenn,
                        It shall clasp a sainted maiden whom the angels name Lenore-
                    Clasp a rare and radiant maiden whom the angels name Lenore."
                                Quoth the Raven "Nevermore."

                        "Be that word our sign of parting, bird or fiend!" I shrieked, upstarting-
                    "Get thee back into the tempest and the Night's Plutonian shore!
                        Leave no black plume as a token of that lie thy soul hath spoken!
                        Leave my loneliness unbroken!-quit the bust above my door!
                    Take thy beak from out my heart, and take thy form from off my door!"
                                Quoth the Raven "Nevermore."

                        And the Raven, never flitting, still is sitting, still is sitting
                    On the pallid bust of Pallas just above my chamber door;
                        And his eyes have all the seeming of a demon's that is dreaming,
                        And the lamp-light o'er him streaming throws his shadow on the floor;
                    And my soul from out that shadow that lies floating on the floor
                                Shall be lifted-nevermore!
                    """
        self.in_4 = r"one\two/two(three)three!^Three&FOUR@FOur-four,four;four'five.five_five$five&five"

        self.inputs = (self.in_1, self.in_2, self.in_3, self.in_4)

    def tearDown(self):
        pass

    def test_CalculateHighestFrequency(self):
        expected_answers = (2,3,56,5)
        for answer, input in zip(expected_answers,self.inputs):
                self.assertEqual(self.analyzer.CalculateHighestFrequency(input), answer)

    def test_CalculateFrequencyForWord(self):
        in_4_expected_freq = {'four': 5, 'five': 5, 'three': 3, 'two': 2, 'one': 1}

        in_2_expected_freq = {
        'ut': 3, 'in': 3, 'dolor': 2, 'dolore': 2, 'lorem': 1, 'ipsum': 1, 'sit': 1,
        'amet': 1, 'consectetur': 1, 'adipiscing': 1, 'elit': 1, 'sed': 1, 'do': 1,
        'eiusmod': 1, 'tempor': 1, 'incididunt': 1, 'labore': 1, 'et': 1, 'magna': 1,
        'aliqua': 1, 'enim': 1, 'ad': 1, 'minim': 1, 'veniam': 1, 'quis': 1,
        'nostrud': 1, 'exercitation': 1, 'ullamco': 1, 'laboris': 1, 'nisi': 1,
        'aliquip': 1, 'ex': 1, 'ea': 1, 'commodo': 1, 'consequat': 1, 'duis': 1,
        'aute': 1, 'irure': 1, 'reprehenderit': 1, 'voluptate': 1, 'velit': 1,
        'esse': 1, 'cillum': 1, 'eu': 1, 'fugiat': 1, 'nulla': 1, 'pariatur': 1,
        'excepteur': 1, 'sint': 1, 'occaecat': 1, 'cupidatat': 1, 'non': 1,
        'proident': 1, 'sunt': 1, 'culpa': 1, 'qui': 1, 'officia': 1, 'deserunt': 1,
        'mollit': 1, 'anim': 1, 'id': 1, 'est': 1, 'laborum': 1 }

        for word, freq in in_4_expected_freq.items():
            self.assertEqual(self.analyzer.CalculateFrequencyForWord(self.in_4, word), freq)
        for word, freq in in_2_expected_freq.items():
            self.assertEqual(self.analyzer.CalculateFrequencyForWord(self.in_2, word), freq)


    def test_CalculateMostFrequentNWords(self):
        in_4_expected_freqN = {5:['four', 'five'], 3:['three',], 2:['two',], 1:['one',]}
        in_2_expected_freqN = {
        3: ['ut', 'in'],
        2: ['dolor', 'dolore'],
        1: ['lorem', 'ipsum', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit',
        'sed', 'do', 'eiusmod', 'tempor', 'incididunt', 'labore', 'et', 'magna',
        'aliqua', 'enim', 'ad', 'minim', 'veniam', 'quis', 'nostrud', 'exercitation',
        'ullamco', 'laboris', 'nisi', 'aliquip', 'ex', 'ea', 'commodo', 'consequat',
        'duis', 'aute', 'irure', 'reprehenderit', 'voluptate', 'velit', 'esse',
        'cillum', 'eu', 'fugiat', 'nulla', 'pariatur', 'excepteur', 'sint',
        'occaecat', 'cupidatat', 'non', 'proident', 'sunt', 'culpa', 'qui',
        'officia', 'deserunt', 'mollit', 'anim', 'id', 'est', 'laborum']
        }

        for freq, words in in_4_expected_freqN.items():
            self.assertEqual(self.analyzer.CalculateMostFrequentNWords(self.in_4, freq), words)
        for freq, words in in_2_expected_freqN.items():
            self.assertEqual(self.analyzer.CalculateMostFrequentNWords(self.in_2, freq), words)

        self.assertEqual(self.analyzer.CalculateMostFrequentNWords(self.in_4, 0), [])
        self.assertEqual(self.analyzer.CalculateMostFrequentNWords(self.in_4, 99), [])

    def test_EmptyInput(self):
        emptyInput = ""
        self.assertEqual(self.analyzer.CalculateHighestFrequency(emptyInput),0)
        self.assertEqual(self.analyzer.CalculateFrequencyForWord(emptyInput,'python'),0)
        for i in range(100):
            self.assertEqual(self.analyzer.CalculateMostFrequentNWords(emptyInput, i),[])

    def test_UnrecognizedCharacter(self):
        in_5 = "python is the best language ever"
        in_6 = "python3 is even better"

        with self.assertRaises(iWordFrequencyAnalyzer.CharacterError):
            self.analyzer.CalculateHighestFrequency(in_6)

        try:
            self.analyzer.CalculateFrequencyForWord(in_5, 'is')
        except iWordFrequencyAnalyzer.CharacterError:
            self.fail("CharacterError raised but unexpected")


    def test_FindEmptyWord(self):
        for input in self.inputs:
            self.assertEqual(self.analyzer.CalculateFrequencyForWord(input,''),0)

    def test_AdjustedSeparator(self):
        new_separators = r'"-.,:;!?\' \n'
        new_analyzer = iWordFrequencyAnalyzer.iWordFrequencyAnalyzer(new_separators)
        for input in self.inputs[:-1]:
            self.assertEqual(new_analyzer.CalculateFrequencyForWord(input,'python'),0)
        with self.assertRaises(iWordFrequencyAnalyzer.CharacterError):
            new_analyzer.CalculateHighestFrequency(self.in_4)


if __name__ == '__main__':
    unittest.main()
