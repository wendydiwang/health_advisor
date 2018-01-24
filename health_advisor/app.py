import wegene


no_running_image = '/path/to/a/running/gif'
no_soda_image = '...'


risk = {
  "description": "痛风",
  "caseid": 88,
  "risk": 0.31,
  "percent": "0.0173",
  "genotypes": [
    {
      "rsid" : "RS6855911",
      "genotype" : "AG",
      "gene" : "IMDB"
    },
    {
      "rsid" : "RS1165205",
      "genotype" : "AA"
    },
    {
      "rsid" : "RS2231142",
      "genotype" : "GG"
    },
    {
      "rsid" : "RS16890979",
      "genotype" : "CT"
    },
    {
      "rsid" : "RS12498742",
      "genotype" : "AG"
    },
    {
      "rsid" : "RS150414818",
      "genotype" : "--"
    }
  ]
}


def get_plan(user_info):
    image_path = None
    advice = None

    try:
        #risk = wegene.Risk().get_risk(profile_id, 88)
    except Exception as e:
        print e.response_body

    if

    return image_path, advice

















wegene.Configuration.o_auth_access_token = '<A valid token with proper scope>'

profile_id = ''
try:
    user = wegene.WeGeneUser().get_user()
    profile_id = user.profiles[0].id
    print profile_id
except Exception as e:
    print e.response_body

try:
    risk = wegene.Risk().get_risk(profile_id, 88)
    print risk
except Exception as e:
    print e.response_body

try:
    athletigen = wegene.Athletigen().get_athletigen(profile_id, 1487)
    print athletigen
except Exception as e:
    print e.response_body

try:
    ancestry = wegene.Ancestry().get_ancestry(profile_id)
    print ancestry
except Exception as e:
    print e.response_body

try:
    haplogroups = wegene.Haplogroups().get_haplogroups(profile_id)
    print haplogroups
except Exception as e:
    print e.response_body

try:
    drug = wegene.Health().get_drug(profile_id, 1481)
    print drug
except Exception as e:
    print e.response_body

try:
    metabolism = wegene.Health().get_metabolism(profile_id, 5)
    print metabolism
except Exception as e:
    print e.response_body

try:
    carrier = wegene.Health().get_carrier(profile_id, 184)
    print carrier
except Exception as e:
    print e.response_body

try:
    traits = wegene.Health().get_traits(profile_id, 34)
    print traits
except Exception as e:
    print e.response_body

try:
    advice = wegene.Sport().get_advice(profile_id, 'man', 26, 174, 84, 'slimming')
    print advice.total_intake
except Exception as e:
    print e.response_body

try:
    allele = wegene.Allele().get_allele(profile_id, ['rs671'])
    print allele
except Exception as e:
    print e.response_body