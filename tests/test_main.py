import unittest
from io import StringIO
from unittest.mock import patch

from SNAWG import WGMO


class TestWGMO(unittest.TestCase):

    @patch('builtins.input', side_effect=['n'])
    @patch('WGMO.private_key_gen')
    @patch('WGMO.public_key_gen')
    @patch('WGMO.sna_labs_connect')
    @patch('WGMO.conf_code_replace_up')
    @patch('sys.stdout', new_callable=StringIO)
    def test_wireguard_not_configured(self, mock_stdout, mock_conf_code_replace_up,
                                      mock_sna_labs_connect, mock_public_key_gen,
                                      mock_private_key_gen, mock_input):
        WGMO.main()
        self.assertIn('Your OS information:', mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['y'])
    @patch('subprocess.run')
    def test_start_connection(self, mock_run, mock_input):
        mock_run.return_value = None
        WGMO.startConnection()
        mock_run.assert_called_with(['sudo', 'wg-quick', 'up', 'wg0'])

    @patch('builtins.input', side_effect=['y'])
    @patch('subprocess.run')
    def test_stop_connection(self, mock_run, mock_input):
        mock_run.return_value = None
        WGMO.stopConnection()
        mock_run.assert_called_with(['sudo', 'wg-quick', 'down', 'wg0'])

    @patch('builtins.input', side_effect=['y'])
    @patch('subprocess.run')
    @patch('sys.stdout', new_callable=StringIO)
    def test_status(self, mock_stdout, mock_run, mock_input):
        mock_run.return_value.stdout = 'interface: wg0\n'
        WGMO.status()
        self.assertIn('Wireguard connection status: connected', mock_stdout.getvalue())

