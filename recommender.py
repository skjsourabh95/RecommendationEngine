
from collections import OrderedDict

def recommend_members(model, challenge_skills, profiles):
    """recommend top 60 members for a challenge given a member slice"""
    top_members = {}
    
    for member,skills in profiles.items():
        if skills:
            member_skills = {}
            for skill in skills:
                member_skills[skill['skill']] = skill['skill_confidence']
            similarity = get_skill_vector(challenge_skills['skills'],member_skills)
            prediction = model.predict(challenge_skills['id'],member,parse_values(similarity)).est
            top_members[member] = prediction * similarity
        
    top_members = OrderedDict({k: v for k, v in sorted(top_members.items(), key=lambda item: item[1],reverse=True)})

    return list(top_members.keys())[:60]

def get_challenges(challenge_profiles):
    """returns a dict of challenge_ids and skills"""
    profiles = []
    for challenges in challenge_profiles:
        skills = [skill['tag'] for skill in challenges['skills']]
        profiles.append({'id':challenges['id'],'skills':skills})

    return profiles
    
def get_skill_vector(challenge_skills,member_skills): 
    """Take average score of a challenge skill against a member skills"""
    val = 0
    count=0 
    
    if challenge_skills and member_skills:
        for skill in challenge_skills:
            if skill in member_skills:
                val+= member_skills[skill]
                count+=1
  
    if val and count: 
        return val/count
    else:
        return 0


def parse_values(x):
    """parsing the similarity score into ratings for the model"""
    if x> 0 and x < 0.3:
        return 1
    elif x>= 0.3 and x < 0.6:
        return 2
    elif x>= 0.6 and x < 0.9:
        return 3
    elif x>=0.9 and x < 1.5:
        return 4
    elif x>=1.5:
        return 5
    else:
        return 0