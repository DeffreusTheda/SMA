# - Settings
### --- Roles 
- Administrator ^843c94
	- Members: squackboost, TahooBulat#4164, kerakel, deffreus
- Moderator
	- Members: deffreus
- Extracurricular
	- Arts & Music
		- Karawitan
		- Gesu Teater
		- Foto-Sinema
	- Fisik
		- PMR
		- Taekwondo
		- Swimming
		- Basket
		- Panahan
		- Badminton
		- Pecinta Alam
		- Paskib
	- Bahasa
		- Broadcasting
		- Jurnalism
		- French
		- Debat Bahasa Indonesia
		- English Debate
		- 日本語
	- Lomba
		- OSN Kimia
		- OSN Ekonomi
		- OSN Informatika
		- OSN Matematika
		- KIR
		- OSN Astronomi
		- OSN Biology
# - Channels
```
#r = rules; #f = forum; #c = text; #v = voice; #s = stage; #t = threads
isSimilar(forum, threads) == true; // diff = ((forum, perma), (threads, tmp))

- EXAMPLE CATEGORIES
	- \#t channel1
		(read)(write)(edit) (read)(write)(edit)     [roles] 
		/^^^^^^^^^^^^^^^^^\ /^^^^^^^^^^^^^^^^^\                     
		permission_of_roles permission_of_@everyone                
		 
		(private|public) : [roles and users]
		/^^^^^^^^^^^^^^\ /^^^^^^^^^^^^^^^^^\
		 accessability       if_private
		 
		// [description]
```

- IMPORTANT
	- \#r welcome-and-rules
		rwxr-- moderator
	- \#c faq
	- \#c roles-assignment
		rwxr-- moderator
	- \#c announcements
		rwxrw- moderator
		// anyone can post
	- \#c hyperlinks
	 - \#c happy-birthday
- MODS ONLY
	- \#c moderator-only
		rwx--- moderator
		private: [Administrator]([[#^843c94]]), squackboost
- SCHOOL
	- \#c general
		// anything
		- \#t classses
	- \#t study-help
	- \#f ib-subjects
	- \#f extracurriculars
	- \#t univ-major-dreams
		// can be \#t, need more discussion
- OFF-TOPIC
	- \#c memes
	- \#t media
	- \#f gaming
	- \#t social-media
	- \#c anarchy
- TECHNICAL
	- \#c suggestions
	- \#c suggestions-poll
	- \#c bots
- VOICE CHANNELS
	- \#f no-mic
	- \#v\ Lounge
	- \#v\ Study Room 1
	- \#v\ Study Room 2
	- \#v Chill
	- \#s In case someone asked where's the stage

```
--------tmp--------
view channel, manage role/permission, manage channel
-------------------
```