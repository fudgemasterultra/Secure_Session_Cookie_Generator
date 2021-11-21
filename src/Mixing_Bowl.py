import uuid, hashlib, platform, time, string, random
#The purpose of this to take some of the work out of making your own secure cookies for user sessions. This helps by pseudo random seed generation. 
# Although not perfect this should be a good starting point.

class GetIngrediants():

    def __init__(self, raisins=None):
        self.salt = str(time.time_ns())
        self.milk = str(uuid.uuid1().int)
        self.eggs = str(uuid.uuid4().int)
        self.butter = str(uuid.getnode())
        self.white_sugar = str(uuid.NAMESPACE_DNS)
        self.brown_sugar = platform.processor()
        self.vanilla_extract = platform.machine()
        self.all_purpose_flour = platform.platform()
        self.baking_soda =  str(platform.uname())
        self.ground_cinnamon = list(string.ascii_letters + string.digits + string.punctuation)
        self.rolled_oats = str(time.time_ns())
        #Ground_cinnamon is used as the legal characters
        random.shuffle(self.ground_cinnamon)
        if raisins == None:
            self.raisins = ""
            for i in range(100):
                self.raisins = self.raisins + random.choice(self.ground_cinnamon)
        else:
            try:
                self.raisins = str(raisins)
            except:
                raise('Raisins requires a str data type or something that can be changed into a str.')
        self.__mix_bowl()
    
    def __mix_bowl(self):
        self.add_to_bowl = list(self.salt + self.white_sugar + self.brown_sugar +  self.all_purpose_flour 
        + self.baking_soda + str(self.ground_cinnamon) + self.rolled_oats + self.raisins + self.milk  + self.eggs + self.butter + self.vanilla_extract)
        #Mixing commenses
        random.shuffle(self.add_to_bowl)
        #Now just make sure it's all nice an homogeneous
        self.batter = hashlib.sha256(str(self.add_to_bowl).encode()).hexdigest()
    
    def Bake_Cookies(self, cookie_size=300):
        if isinstance(cookie_size, int) == False:
            raise("Size must be an int")
        if cookie_size <= 0:
            raise("Cookie must have a size of atleast 1.")
        
        more_batter = str(time.time_ns()).encode()
        self.batter = hashlib.sha256(more_batter + self.batter.encode()).hexdigest()
        random.seed(self.batter)
        random.shuffle(self.ground_cinnamon)
        cookie = ""
        for i in range(cookie_size):
            cookie = cookie + random.choice(self.ground_cinnamon)
        return cookie

        

        