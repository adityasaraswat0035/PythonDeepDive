import os
import unittest
class TextAnalysisTest(unittest.TestCase):
    """Tests for the ``analyze_text()`` function."""

    def setUp(self):
        "Fixture that creates a file for the text methods to use."
        self.filename="text_analysis_test_file.txt"
        with open(self.filename,mode="wt",encoding="utf-8") as fh:
            fh.write('Now we are engaged in a great civil war,\n'
                    'testing whether that nation,\n'
                    'or any nation so conceived and so dedicated,\n'
                    'can long endure.')
    

    def tearDown(self):
        "Fixture that deletes the files used by the test methods."
        try:
            os.remove(self.filename)
        except OSError:
            pass


    def test_function_run(self):
        """Basic smoke test: does the function run."""
        self.analyze_text(self.filename)


    def test_line_count(self):
        "Check that the line count is correct."
        self.assertEqual(self.analyze_text(self.filename)[0],4)


    def test_character_count(self):
        "Check that chacter count is correct."
        self.assertEqual(self.analyze_text(self.filename)[1],131)


    def test_no_such_file(self):
        "Check the proper exception is thrown for a missing file."
        with self.assertRaises(IOError):
            self.analyze_text("foobar")
    def test_no_deletion(self):
        "Check that the function doesn't delete the input file."
        self.analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))

    def analyze_text(self,filename):
        """Calculate the number of lines and characters in a file.
        Args:
            filename: The name of the file to analyze.
        Raises:
            IOError: If ``filename`` does not exist or can't be read.Returns: The number of lines in the file.
        """
        lines=0
        characters=0
        with open(filename,'r') as f:
            for line in f:
                lines+=1
                characters+=len(line)
        return (lines,characters)
    
    

    

if __name__=="__main__":
    unittest.main()
