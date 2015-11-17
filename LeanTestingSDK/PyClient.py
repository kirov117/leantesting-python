import sys
import os

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))) # adds current SDK path to sys.path for imports

#TODO PyPI python package index compatibility

from Handler.Auth.OAuth2Handler				import OAuth2Handler
from Handler.User.UserHandler				import UserHandler
from Handler.Project.ProjectsHandler		import ProjectsHandler
from Handler.Bug.BugsHandler				import BugsHandler
from Handler.Attachment.AttachmentsHandler	import AttachmentsHandler
from Handler.Platform.PlatformHandler		import PlatformHandler

class PyClient:
	"""

	Lean Testing Python Client SDK

	https://leantesting.com/en/api-docs Adheres to official API guidelines

	"""

	_accessToken  = None

	auth		  = None
	user		  = None
	projects	  = None
	bugs		  = None
	attachments	  = None
	platform	  = None

	def __init__(self):
		"""

		Constructs a PyClient instance

		Keyword arguments:
		self PyClient -- Self instance

		"""

		self.auth			= OAuth2Handler(self)
		self.user			= UserHandler(self)
		self.projects		= ProjectsHandler(self)
		self.bugs			= BugsHandler(self)
		self.attachments	= AttachmentsHandler(self)
		self.platform		= PlatformHandler(self)

	def getCurrentToken(self):
		"""

		Function to retrieve curently attached token.

		Keyword arguments:
		self PyClient -- Self instance

		Returns:
		str     -- if a token is attached
		boolean -- if no token is attached

		"""

		if self._accessToken is None:
			return False

		return self._accessToken

	def attachToken(self, accessToken):
		"""

		Function to attach new token to SDK Client instance. Token changes are dynamic; all objects/entities
		originating from an instance which has had its token updated will utilize the new token automatically.

		Keyword arguments:
		self        PyClient -- Self instance
		accessToken str      -- the string of the token to be attached

		"""

		self._accessToken = accessToken
