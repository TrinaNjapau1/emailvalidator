"""  Unit tests for checking e-mail validator  """
import unittest
import string
from email_validator import check_email


class TestSequenceFunctions(unittest.TestCase):
    """     This class contains the following test-methods:
    1) test_check_email_parts_ok - Check @ in e-mail (ok cases);
    2) test_check_email_parts_raises - Check @ in e-mail (raise cases);
    3) test_domain_len_ok - Check len of domain = (3, 256) (ok cases);
    4) test_domain_len_raises - Check len of domain = (3, 256) (raise cases);
    5) test_domain_non_empty_ok - Check a set of non-empty rows of domain (ok cases);
    6) test_domain_non_empty_raises - Check a set of non-empty rows of domain (raise cases);
    7) test_domain_symbols_ok - Check symbols = [a-z0-9_-] in domain (ok cases);
    8) test_domain_symbols_raises - Check wrong symbols =
       ("#","$","/",...,[A-Z]) in domain (raise cases);
    9) test_domain_dash_raises - Check starts/ends "-" in domain (raise cases);
    10) test_username_len_ok - Check len of username = (1,128) (ok cases);
    def test_username_len_raises - Check len of username = (1,128) (raise cases);
    11) test_username_symbols_ok - Check symbols = [a-z0-9._-] in username (ok cases);
    12) test_username_symbols_raises -Check wrong symbols =
        ("#","$","/",...,[A-Z]) in username (raise cases);
    13) test_username_points_raises - Check two consecutive points in name (raise cases);
    14) test_username_dbl_quotes_ok - Check the paired double quotes (ok cases);
    15) test_username_dbl_quotes_raises - Check the paired double quotes (raise cases);
    16) test_username_proh_sym_ok - Check prohibited symbols
        between paired double quotes (ok cases);
    17) test_username_proh_sym_raises - heck prohibited symbols
        between paired double quotes (raise cases);
    """

    def test_check_email_parts_ok(self):
        """  Check @ in e-mail (Task 1.1)  """

        cases = ["123345nnbh@dfg.com", "_15nh@dfg.com.sd", "12.n-nbh@dfg.c_om"]
        for case in cases:
            self.assertTrue(check_email(case))

    def test_check_email_parts_raises(self):
        """  Check @ in e-mail (Task 1.2)  """

        cases = ["123345nnbh.dfg.com", "@dfg.com", "dfg.com@"]
        for case in cases:
            self.assertRaises(ValueError, check_email, case)

    def test_domain_len_ok(self):
        """  Check len of domain = (3, 256) (Task 2.1)  """

        cases = ["user_name@s.c",
                 "user_name@domain.com",
                 "user_name@a." + ("b" * 254),
                 "user_name@a." + ("b" * 253),
                 "user_name@" + ("b" * 254) + ".a",
                 "user_name@" + ("b" * 253) + ".a"]
        for case in cases:
            self.assertTrue(check_email(case))

    def test_domain_len_raises(self):
        """  Check len of domain = (3, 256) (Task 2.2)  """

        cases = ["user_name@.f",
                 "user_name@a." + ("b" * 255),
                 "user_name@a." + ("b" * 1000),
                 "user_name@" + ("b" * 255) + ".a",
                 "user_name@" + ("b" * 1000) + ".a"]
        for case in cases:
            self.assertRaises(ValueError, check_email, case)

    def test_domain_non_empty_ok(self):
        """  Check a set of non-empty rows of domain (Task 2.3)  """

        cases = ["user_name@domain.com",
                 "user_name@do.main.com",
                 "user_name@d.o.m.a.i.n.com.ru"]
        for case in cases:
            self.assertTrue(check_email(case))

    def test_domain_non_empty_raises(self):
        """  Check a set of non-empty rows of domain (Task 2.4)  """

        cases = ["user_name@s.", "user_name@.s",
                 "user_name@.", "user_name@s.s.",
                 "user_name@.s.s.s", "user_name@.s.s.s."]
        for case in cases:
            self.assertRaises(ValueError, check_email, case)

    def test_domain_symbols_ok(self):
        """  Check symbols = [a-z0-9_-] in domain (Task 2.5)  """

        cases = [
            "user_name@abc.abc.abc",
            "user_name@" +
            string.ascii_lowercase +
            "." +
            string.ascii_lowercase,
            "user_name@" +
            string.digits +
            "." +
            string.digits,
            "user_name@123.123.123",
            "user_name@abc_-123.abc_-123.abc_-123",
            "user_name@__abc-123.__abc-123__.abc-123",
            "user_name@abc-123.__abc-123__.abc-123__",
            "user_name@___.___.___"]
        for case in cases:
            self.assertTrue(check_email(case))

    def test_domain_symbols_raises(self):
        """  Check wrong symbols = ("#","$","/",...,[A-Z]) in domain (Task 2.6)  """

        cases = ["user_name@ab#c.a#bc.a#bc", "user_name@#.#.#",
                 "user_name@ab$c.a$bc.a$bc", "user_name@$.$.$",
                 "user_name@ab/c.a/bc.a/bc", "user_name@/././",
                 "user_name@abc.ABC.abc", "user_name@ABC.abc.abc",
                 "user_name@abc.abc.ABC"]
        for case in cases:
            self.assertRaises(ValueError, check_email, case)

    def test_domain_dash_raises(self):
        """  Check starts/ends "-" in domain (Task 3.1)  """

        cases = ["user_name@-abc1_.abc1_", "user_name@abc1_-.abc1_",
                 "user_name@abc1_.-abc1_", "user_name@abc1_.abc1_-",
                 "user_name@-abc1_-.-abc1_-", "user_name@abc1_.-abc1_-.abc1_",
                 "user_name@-.abc1_.-", "user_name@abc1_.-.abc1_",
                 "user_name@---.---.---"]
        for case in cases:
            self.assertRaises(ValueError, check_email, case)

    def test_username_len_ok(self):
        """  Check len of username = (1,128) (Task 4.1)  """

        cases = [string.ascii_lowercase + string.digits + "@domain.com",
                 "b@dfg.com",
                 ("a" * 127) + "@domain.com",
                 ("a" * 128) + "@domain.com"]
        for case in cases:
            self.assertTrue(check_email(case))

    def test_username_len_raises(self):
        """  Check len of username = (1,128) (Task 4.2)  """

        cases = [("a" * 129) + "@domain.com",
                 ("a" * 1000) + "@domain.com"]
        for case in cases:
            self.assertRaises(ValueError, check_email, case)

    def test_username_symbols_ok(self):
        """  Check symbols = [a-z0-9._-] in username (Task 4.3)  """

        cases = [string.ascii_lowercase + "@domain.com",
                 string.digits + "@domain.com",
                 string.ascii_lowercase + string.digits + "@domain.com",
                 ".dfg12dg.df12g.@domain.com",
                 "-dfg12dg-df12g-@domain.com",
                 "_dfg12dg_df12g_@domain.com",
                 ".-_dfg12dg.-_df12g.-_@domain.com",
                 ".___.__.--.--.___.__.---@domain.com",
                 "_@domain.com", "-@domain.com", ".@domain.com"]
        for case in cases:
            self.assertTrue(check_email(case))

    def test_username_symbols_raises(self):
        """  Check wrong symbols = ("#","$","/",...,[A-Z]) in username (Task 4.4)  """

        cases = ["#sdhgf#ghg11#@domain.com", "###@domain.com",
                 "$sdhgf$ghg11$@domain.com", "$$$@domain.com",
                 "/sdhgf/ghg11/@domain.com", "///@domain.com",
                 "ADF.adf@domain.com", "adf.ADF@domain.com",
                 "adf_ADF_adf@domain.com"]
        for case in cases:
            self.assertRaises(ValueError, check_email, case)

    def test_username_points_raises(self):
        """  Check two consecutive points in name (Task 5.1)  """

        cases = ["..dfg12dg-df12g-@domain.com",
                 "_dfg12dg_df12g..@domain.com",
                 ".-_dfg12dg..df12g.-_@domain.com",
                 "......@domain.com", "..@domain.com"]
        for case in cases:
            self.assertRaises(ValueError, check_email, case)

    def test_username_dbl_quotes_ok(self):
        """  Check the paired double quotes (Task 6.1)  """

        cases = ['"as"dsdf12"12"@domain.com',
                 '""dsd""f12""@domain.com',
                 '""""""@domain.com']
        for case in cases:
            self.assertTrue(check_email(case))

    def test_username_dbl_quotes_raises(self):
        """  Check the paired double quotes (Task 6.2)  """

        cases = ['"asdsdf1212@domain.com', 'dsd"f12@domain.com',
                 'dsdf12"@domain.com', '"""@domain.com']
        for case in cases:
            self.assertRaises(ValueError, check_email, case)

    def test_username_proh_sym_ok(self):
        """  Check prohibited symbols between paired double quotes (Task 7.1)  """

        cases = ['as"!"as"vc"@domain.com',
                 'as":"as"vc"@domain.com',
                 'as","as"vc"@domain.com',
                 '"!!!!!"@domain.com',
                 '",,,,,"@domain.com',
                 '":::::"@domain.com']
        for case in cases:
            self.assertTrue(check_email(case))

    def test_username_proh_sym_raises(self):
        """  Check prohibited symbols between paired double quotes (Task 7.2)  """
        cases = ['a!!!s"ds!!!df12"1!!!2@domain.com',
                 'a,,,s"ds,,,df12"1,,,2@domain.com',
                 'a:::s"ds:::df12"1:::2@domain.com',
                 '!!!!!@domain.com', ',,,,,@domain.com',
                 ':::::@domain.com']
        for case in cases:
            self.assertRaises(ValueError, check_email, case)

if __name__ == '__main__':
    # Runs unit tests 
    unittest.main()
