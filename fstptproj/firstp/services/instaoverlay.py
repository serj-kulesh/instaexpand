"""
    Expand functionality InstagramAPI 
"""

from InstagramAPI import InstagramAPI


class IOverlay(InstagramAPI):
    """ 
        InstagramAPI overlay to call functions without 
        calling api.LastJson everytime
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def SendRequest(self, *args, **kwargs):
        super().SendRequest(*args, **kwargs)
        return self.LastJson
        
    
    def autoCompleteUserList(self, *args, **kwargs):
        super().autoCompleteUserList(*args, **kwargs)
        return self.LastJson
        
    
    def backup(self, *args, **kwargs):
        super().backup(*args, **kwargs)
        return self.LastJson
        
    
    def block(self, *args, **kwargs):
        super().block(*args, **kwargs)
        return self.LastJson
        
    
    def buildBody(self, *args, **kwargs):
        super().buildBody(*args, **kwargs)
        return self.LastJson
        
    
    def changePassword(self, *args, **kwargs):
        super().changePassword(*args, **kwargs)
        return self.LastJson
        
    
    def changeProfilePicture(self, *args, **kwargs):
        super().changeProfilePicture(*args, **kwargs)
        return self.LastJson
        
    
    def comment(self, *args, **kwargs):
        super().comment(*args, **kwargs)
        return self.LastJson
        
    
    def configure(self, *args, **kwargs):
        super().configure(*args, **kwargs)
        return self.LastJson
        
    
    def configureTimelineAlbum(self, *args, **kwargs):
        super().configureTimelineAlbum(*args, **kwargs)
        return self.LastJson
        
    
    def configureVideo(self, *args, **kwargs):
        super().configureVideo(*args, **kwargs)
        return self.LastJson
        
    
    def deleteComment(self, *args, **kwargs):
        super().deleteComment(*args, **kwargs)
        return self.LastJson
        
    
    def deleteMedia(self, *args, **kwargs):
        super().deleteMedia(*args, **kwargs)
        return self.LastJson
        
    
    def direct_share(self, *args, **kwargs):
        super().direct_share(*args, **kwargs)
        return self.LastJson
        
    
    def editMedia(self, *args, **kwargs):
        super().editMedia(*args, **kwargs)
        return self.LastJson
        
    
    def editProfile(self, *args, **kwargs):
        super().editProfile(*args, **kwargs)
        return self.LastJson
        
    
    def explore(self, *args, **kwargs):
        super().explore(*args, **kwargs)
        return self.LastJson
        
    
    def expose(self, *args, **kwargs):
        super().expose(*args, **kwargs)
        return self.LastJson
        
    
    def fbUserSearch(self, *args, **kwargs):
        super().fbUserSearch(*args, **kwargs)
        return self.LastJson
        
    
    def follow(self, *args, **kwargs):
        super().follow(*args, **kwargs)
        return self.LastJson
        
    
    def generateDeviceId(self, *args, **kwargs):
        super().generateDeviceId(*args, **kwargs)
        return self.LastJson
        
    
    def generateSignature(self, *args, **kwargs):
        super().generateSignature(*args, **kwargs)
        return self.LastJson
        
    
    def generateUUID(self, *args, **kwargs):
        super().generateUUID(*args, **kwargs)
        return self.LastJson
        
    
    def generateUploadId(self, *args, **kwargs):
        super().generateUploadId(*args, **kwargs)
        return self.LastJson
        
    
    def getDirectShare(self, *args, **kwargs):
        super().getDirectShare(*args, **kwargs)
        return self.LastJson
        
    
    def getFollowingRecentActivity(self, *args, **kwargs):
        super().getFollowingRecentActivity(*args, **kwargs)
        return self.LastJson
        
    
    def getGeoMedia(self, *args, **kwargs):
        super().getGeoMedia(*args, **kwargs)
        return self.LastJson
        
    
    def getHashtagFeed(self, *args, **kwargs):
        super().getHashtagFeed(*args, **kwargs)
        return self.LastJson
        
    
    def getLikedMedia(self, *args, **kwargs):
        super().getLikedMedia(*args, **kwargs)
        return self.LastJson
        
    
    def getLocationFeed(self, *args, **kwargs):
        super().getLocationFeed(*args, **kwargs)
        return self.LastJson
        
    
    def getMediaComments(self, *args, **kwargs):
        super().getMediaComments(*args, **kwargs)
        return self.LastJson
        
    
    def getMediaLikers(self, *args, **kwargs):
        super().getMediaLikers(*args, **kwargs)
        return self.LastJson
        
    
    def getPopularFeed(self, *args, **kwargs):
        super().getPopularFeed(*args, **kwargs)
        return self.LastJson
        
    
    def getProfileData(self, *args, **kwargs):
        super().getProfileData(*args, **kwargs)
        return self.LastJson
        
    
    def getRecentActivity(self, *args, **kwargs):
        super().getRecentActivity(*args, **kwargs)
        return self.LastJson
        
    
    def getSelfGeoMedia(self, *args, **kwargs):
        super().getSelfGeoMedia(*args, **kwargs)
        return self.LastJson
        
    
    def getSelfSavedMedia(self, *args, **kwargs):
        super().getSelfSavedMedia(*args, **kwargs)
        return self.LastJson
        
    
    def getSelfUserFeed(self, *args, **kwargs):
        super().getSelfUserFeed(*args, **kwargs)
        return self.LastJson
        
    
    def getSelfUserFollowers(self, *args, **kwargs):
        super().getSelfUserFollowers(*args, **kwargs)
        return self.LastJson
        
    
    def getSelfUserTags(self, *args, **kwargs):
        super().getSelfUserTags(*args, **kwargs)
        return self.LastJson
        
    
    def getSelfUsernameInfo(self, *args, **kwargs):
        super().getSelfUsernameInfo(*args, **kwargs)
        return self.LastJson
        
    
    def getSelfUsersFollowing(self, *args, **kwargs):
        super().getSelfUsersFollowing(*args, **kwargs)
        return self.LastJson
        
    
    def getTimeline(self, *args, **kwargs):
        super().getTimeline(*args, **kwargs)
        return self.LastJson
        
    
    def getTotalFollowers(self, *args, **kwargs):
        super().getTotalFollowers(*args, **kwargs)
        return self.LastJson
        
    
    def getTotalFollowings(self, *args, **kwargs):
        super().getTotalFollowings(*args, **kwargs)
        return self.LastJson
        
    
    def getTotalLikedMedia(self, *args, **kwargs):
        super().getTotalLikedMedia(*args, **kwargs)
        return self.LastJson
        
    
    def getTotalSelfFollowers(self, *args, **kwargs):
        super().getTotalSelfFollowers(*args, **kwargs)
        return self.LastJson
        
    
    def getTotalSelfFollowings(self, *args, **kwargs):
        super().getTotalSelfFollowings(*args, **kwargs)
        return self.LastJson
        
    
    def getTotalSelfUserFeed(self, *args, **kwargs):
        super().getTotalSelfUserFeed(*args, **kwargs)
        return self.LastJson
        
    
    def getTotalUserFeed(self, *args, **kwargs):
        super().getTotalUserFeed(*args, **kwargs)
        return self.LastJson
        
    
    def getUserFeed(self, *args, **kwargs):
        super().getUserFeed(*args, **kwargs)
        return self.LastJson
        
    
    def getUserFollowers(self, *args, **kwargs):
        super().getUserFollowers(*args, **kwargs)
        return self.LastJson
        
    
    def getUserFollowings(self, *args, **kwargs):
        super().getUserFollowings(*args, **kwargs)
        return self.LastJson
        
    
    def getUserTags(self, *args, **kwargs):
        super().getUserTags(*args, **kwargs)
        return self.LastJson
        
    
    def getUsernameInfo(self, *args, **kwargs):
        super().getUsernameInfo(*args, **kwargs)
        return self.LastJson
        
    
    def getv2Inbox(self, *args, **kwargs):
        super().getv2Inbox(*args, **kwargs)
        return self.LastJson
        
    
    def getv2Threads(self, *args, **kwargs):
        super().getv2Threads(*args, **kwargs)
        return self.LastJson
        
    
    def like(self, *args, **kwargs):
        super().like(*args, **kwargs)
        return self.LastJson
        
    
    def login(self, *args, **kwargs):
        super().login(*args, **kwargs)
        return self.LastJson
        
    
    def logout(self, *args, **kwargs):
        super().logout(*args, **kwargs)
        return self.LastJson
        
    
    def mediaInfo(self, *args, **kwargs):
        super().mediaInfo(*args, **kwargs)
        return self.LastJson
        
    
    def megaphoneLog(self, *args, **kwargs):
        super().megaphoneLog(*args, **kwargs)
        return self.LastJson
        
    
    def removeProfilePicture(self, *args, **kwargs):
        super().removeProfilePicture(*args, **kwargs)
        return self.LastJson
        
    
    def removeSelftag(self, *args, **kwargs):
        super().removeSelftag(*args, **kwargs)
        return self.LastJson
        
    
    def searchLocation(self, *args, **kwargs):
        super().searchLocation(*args, **kwargs)
        return self.LastJson
        
    
    def searchTags(self, *args, **kwargs):
        super().searchTags(*args, **kwargs)
        return self.LastJson
        
    
    def searchUsername(self, *args, **kwargs):
        super().searchUsername(*args, **kwargs)
        return self.LastJson
        
    
    def searchUsers(self, *args, **kwargs):
        super().searchUsers(*args, **kwargs)
        return self.LastJson
        
    
    def setNameAndPhone(self, *args, **kwargs):
        super().setNameAndPhone(*args, **kwargs)
        return self.LastJson
        
    
    def setPrivateAccount(self, *args, **kwargs):
        super().setPrivateAccount(*args, **kwargs)
        return self.LastJson
        
    
    def setProxy(self, *args, **kwargs):
        super().setProxy(*args, **kwargs)
        return self.LastJson
        
    
    def setPublicAccount(self, *args, **kwargs):
        super().setPublicAccount(*args, **kwargs)
        return self.LastJson
        
    
    def setUser(self, *args, **kwargs):
        super().setUser(*args, **kwargs)
        return self.LastJson
        
    
    def syncFeatures(self, *args, **kwargs):
        super().syncFeatures(*args, **kwargs)
        return self.LastJson
        
    
    def syncFromAdressBook(self, *args, **kwargs):
        super().syncFromAdressBook(*args, **kwargs)
        return self.LastJson
        
    
    def tagFeed(self, *args, **kwargs):
        super().tagFeed(*args, **kwargs)
        return self.LastJson
        
    
    def throwIfInvalidUsertags(self, *args, **kwargs):
        super().throwIfInvalidUsertags(*args, **kwargs)
        return self.LastJson
        
    
    def timelineFeed(self, *args, **kwargs):
        super().timelineFeed(*args, **kwargs)
        return self.LastJson
        
    
    def unblock(self, *args, **kwargs):
        super().unblock(*args, **kwargs)
        return self.LastJson
        
    
    def unfollow(self, *args, **kwargs):
        super().unfollow(*args, **kwargs)
        return self.LastJson
        
    
    def unlike(self, *args, **kwargs):
        super().unlike(*args, **kwargs)
        return self.LastJson
        
    
    def uploadAlbum(self, *args, **kwargs):
        super().uploadAlbum(*args, **kwargs)
        return self.LastJson
        
    
    def uploadPhoto(self, *args, **kwargs):
        super().uploadPhoto(*args, **kwargs)
        return self.LastJson
        
    
    def uploadVideo(self, *args, **kwargs):
        super().uploadVideo(*args, **kwargs)
        return self.LastJson
        
    
    def userFriendship(self, *args, **kwargs):
        super().userFriendship(*args, **kwargs)
        return self.LastJson