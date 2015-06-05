import smtplib
import SMTP_settings


class SendEmail:

    @staticmethod
    def send_email(to, subject, text):
        TO = to
        SUBJECT = subject
        TEXT = text

        # Gmail Sign In

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(SMTP_settings.SMTP_USERNAME, SMTP_settings.SMTP_PASSWORD)

        BODY = '\r\n'.join(['To: %s' % TO,
                            'From: %s' % SMTP_settings.SMTP_USERNAME,
                            'Subject: %s' % SUBJECT,
                            '', TEXT])

        try:
            server.sendmail(SMTP_settings.SMTP_USERNAME, [TO], BODY)
            print ('Email sent')
        except:
            print ('Error sending mail')

        server.quit()
