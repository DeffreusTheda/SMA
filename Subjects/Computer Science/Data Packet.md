Above: [[Packet Switching]], [[Router]]
Related: [[Internet Protocol]], [[Port]], [[Binary]]

Contains:$^1$
	Header
		From: The sender's IP address.
		To: The receiver's IP address, including CC and BCC.
			CC is the carbon copy: the additional destination address for more than one receivers.
			BCC is the blind copy, similar to CC, but doesn't show up in header and is hidden from CC receiver.
		Date: Timestamp, when the email was sent.
		Subject: The subject of the email.
		Return Path: 
			The return address of the reply, a.k.a. "Reply-To". 
			If you reply to an email, the reply will go to the address mentioned in this field.
		Domain Key and DKIM Signatures: Email signatures are provided by email services to identify and authenticate emails.
		SPF: 
			SPF stand for 'Sender Policy Framework'.
			An authentication method used by senders to specify hosts that are allowed to send an email on behalf of the domain.
			It will help to understand if the actual server is used to send the email from a specific domain.
		Message-ID: unique ID of the email.
		MIME-Version: 
			Used MIME version.
			It will help to understand the delivered "non-text" contents and attachments.
		X-Headers:
			The receiver mail providers usually add these fields.
			Provided info is usually experimental and can be different according to the mail provider.
		X-Received: Mail servers that the email went through.
		X-Spam Status: Spam score of the email.
		X-Mailer: Email client name.
	Payload
		Data in the payload is in the form of binary.
		Contains:
			Source Address (IP),
			Target Address (Server name),
			Protocol,
			Data in form of binary. ^873d36

<hr>
References:
1. [IB Computer Science - Topic 3 - Networks](https://www.youtube.com/watch?v=bFkYffPJq0M)
2. [Tryhackme.com](https://tryhackme.com/room/adventofcyber4)