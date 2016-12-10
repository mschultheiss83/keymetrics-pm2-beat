from keymetrics-pm2-beat import BaseTest

import os


class Test(BaseTest):

    def test_base(self):
        """
        Basic test with exiting Keymetrics-pm2-beat normally
        """
        self.render_config_template(
                path=os.path.abspath(self.working_dir) + "/log/*"
        )

        keymetrics-pm2-beat_proc = self.start_beat()
        self.wait_until( lambda: self.log_contains("keymetrics-pm2-beat is running"))
        exit_code = keymetrics-pm2-beat_proc.kill_and_wait()
        assert exit_code == 0
