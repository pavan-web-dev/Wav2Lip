import gdown

LIPSYNC_EXPERT = False
VISUAL_QUALITY_DISC = False
WAV2LIP_GAN = True
WAV2LIP = False


if LIPSYNC_EXPERT:
    url = "https://drive.google.com/uc?id=1beOJgFCbH3eUaqYk5g21wL_kapOzgNgu"
    output = "lipsync_expert.pth"
    gdown.download(url, output)

if VISUAL_QUALITY_DISC:
    url = "https://drive.google.com/uc?id=1GUJJwfXaCDZ8l4bIyR2FbrkT86XI9I1B"
    output = "visual_quality_disc.pth"
    gdown.download(url, output)

if WAV2LIP_GAN:
    url = "https://drive.google.com/uc?id=1Hxl7S0OfRdiwhnyAt0W0fPcknw6tjUib"
    output = "wav2lip_gan.pth"
    gdown.download(url, output)

    
if WAV2LIP:
    url = "https://drive.google.com/uc?id=1WKnimerJEeffifROLrMsgkmbcAaotLbB"
    output = "wav2lip.pth"
    gdown.download(url, output)

    