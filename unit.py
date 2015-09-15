#unit tests
import csv
import unittest
from qualityLife import qualityLife

class qualityLifeTests(unittest.TestCase):
    def test_average(self):
        self.assertEqual(qualityLife.getAverage([1,1,1]), 1.0)
        self.assertEqual(qualityLife.getAverage([1,2,3]), 2.0)
        self.assertEqual(qualityLife.getAverage([3,6,9]), 6.0)
    def test_hardshipIndex(self):
        f=open('income.csv')
        csv_reader=csv.reader(f)
        row=next(csv_reader)
        testPart=row[len(row)-1]
        f.close()
        self.assertEqual(testPart,'HARDSHIP INDEX')#testing to make sure I was indeed accessing the Hardship Index
    def test_recentLifeExpectancy(self):
        f=open('life_expectancy.csv')
        csv_reader=csv.reader(f)
        row=next(csv_reader)
        testPart=row[len(row)-1]
        f.close()
        self.assertEqual(testPart, '2010 Upper 95% CI')
    def test_totalLibraryVisits(self):
        f=open('library_visits.csv')
        csv_reader=csv.reader(f)
        row=next(csv_reader)
        testPart=row[len(row)-1]
        f.close()
        self.assertEqual(testPart, 'YTD')
    def test_simplifyData(self):
        a=[1,2,3]
        b=[1,2,3,4,5,6,7,8,9,10]
        c=[1]
        self.assertEqual(qualityLife.simplifyData(a,b,c),([1,2,3],[1]))
if __name__=='__main__':
    unittest.main()


