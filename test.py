
import unittest
import pandas as pd
import os
from assignment import generate_report

class TestReportAutomation(unittest.TestCase):
    def test_generate_report(self):
        # Create a sample dataframe
        data = {'Sales': [100, 150, 200, 120]}
        df = pd.DataFrame(data)

        output_file = 'test_report.txt'
        generate_report(df, output_file)

        # Check if the file was created and contains the expected content
        self.assertTrue(os.path.exists(output_file))
        with open(output_file, 'r') as f:
            content = f.read()
            self.assertIn("Average Sales: 142.50", content)

        # Clean up the created file
        os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
