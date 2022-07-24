from django.urls import path

from .views import (
    LogInView, SignUpView,LogOutView,linkedin_lix,linkedin_group,linkedin_search,facebook,twitter,accelerators,twitter_web3,Blank,wonderverse,scaleups,founders,data_scientist_phantom,nft_phantom,defi_phantom,dapp_phantom,dao_phantom,yf_phantom,data_scientist_lix,nft_lix,defi_lix,dapp_lix,dao_lix,yf_lix,entrepreneurs,cm_phantom,cb_phantom,cmanag_phantom,dc_phantom,cm_lix,cb_lix,cmanag_lix,dc_lix,entrepreneurs_phantom,founders_phantom,digital_marketing,blockchain,data_analysis,venture_funding,uiux,pm_lix,blockchain_phantom,digital_marketing_phantom,data_analysis_phantom,venture_funding_phantom,uiux_phantom,pm_phantom,cb_twi_view,cg_twi_view,cm_twi_view,twi_marketing_view,web3_com_twi_view,web3_marketing_twi_view,discordbot_twi_view,chatbots_twi_view,vc_lix,angel_lix,sc_lix,fr_lix,pi_lix,vc_phantom,angel_phantom,sc_phantom,fr_phantom,pi_phantom,vc_fb,ai_fb,pd_fb,pi_fb,ba_fb,vc_twi,angeli_twi,sc_twi,wf_twi,wg_twi,fr_twi,wp_twi,pd_twi,pi_twi,ba_twi,wi_twi,design_twi,gd_twi,vd_twi,md_twi,bc_twi,d3_fb,gd_fb,d3_design_lix,gd_lix,vd_lix,md_lix,bc_lix,d3_phantom,gd_phantom,vd_phantom,md_phantom,bc_phantom,ai_phantom,ml_phantom,algo_phantom,dm_phantom,ann_phantom,dp_phantom,ai_lix,ml_lix,algo_lix,dm_lix,ann_lix,dp_lix,angle_investor_fb_view,ml_fb,algo_fb,dm_fb,ann_fb,ai_twi,ml_twi,algo_twi,dm_twi,ann_twi,dp_twi,dmarketing_fb,block_fb,sd_fb,da_fb,ux_ui_fb,enter_fb,uiux_instagram,enter_instagram,dm_instagram,dmar_twi,enter_twi,uxuidesign_twi,figma_lix,notion_lix,slack_lix,trello_lix,miro_lix,micromenter_insta,menterpass_insta,figma_twi,onalytica_twi,slack_twi,trello_twi,miro_twi,notion_twi
        ,micromenter_twi,
        menterpass_twi,figma_phantom,notion_phantom,slack_phantom,trello_phantom,bd_design_lix,bd_design_phantom,mobile_dev_phantom,mobile_dev_lix,Web_dev,web_dev_phantom_display,software_dev_phantom,

        algo_fb_ads,ai_fb_ads,dataanalysis_fb_ads,dm_fb_ads,ml_fb_ads,ann_fb_ads,algo_lix_ads,ai_lix_ads,dataanalysis_lix_ads,dm_lix_ads,dp_lix_ads,ds_lix_ads,ml_lix_ads,ann_lix_ads,algo_phantom_ads,ai_phantom_ads,dataanalysis_phantom_ads,dm_phantom_ads,dp_phantom_ads,ds_phantom_ads,ml_phantom_ads,ann_phantom_ads,algo_twi_ads,ai_twi_ads,dm_twi_ads,dp_twi_ads,ml_twi_ads,ann_twi_ads,

        figma_lix_ads,notion_lix_ads,slack_lix_ads,trello_lix_ads,figma_phantom_ads,notion_phantom_ads,slack_phantom_ads,trello_phantom_ads,figma_twi_ads,miro_twi_ads,notion_twi_ads,onalytica_twi_ads,slack_twi_ads,trello_twi_ads,

        cb_lix_ads,cmanag_lix_ads,cm_lix_ads,dc_lix_ads,cb_phantom_ads,cmanag_phantom_ads,cm_phantom_ads,dc_phantom_ads,chatbot_twi_ads,cb_twi_ads,cg_twi_ads,cm_twi_ads,db_twi_ads,twi_marketing_twi_ads,web3_commu_twi_ads,web3_marketing_twi_ads,

        enterpreneurs_fb_ads,enterpreneurs_lix__ads,founder_lix_ads,enterpreneurs_phantom_ads,founders_phantom_ads,enterpreneurs_twi_ads,

        d3_design_fb_ads,graphic_design_fb_ads,uiux_design_fb_ads,d3_design_lix_ads,brand_designers_lix_ads,branding_consultant_lix_ads,graphic_design_lix_ads,marketing_designer_lix_ads,uiux_lix_ads,visual_design_lix_ads,d3_design_phantom_ads,brand_designers_phantom_ads,branding_consultant_phantom_ads,graphic_design_phantom_ads,marketing_designer_phantom_ads,uiux_design_phantom_ads,visual_design_phantom_ads,d3_design_twi_ads,branding_consultant_twi_ads,graphic_design_twi_ads,marketing_designer_twi_ads,uiux_design_twi_ads,visual_design_twi_ads,

        micromentor_twi_ads,mentorpass_twi_ads,display_count,software,

        digital_marketing_fb_ads,digital_marketing_lix_ads,digital_marketing_phantom_ads,digital_marketing_twi_ads,
        pm_fit_lix_ads,pm_fit_phantom_ads,
        software_development_fb_ads,mobile_development_lix_ads,software_development_lix_ads,web_development_lix_ads,mobile_development_phantom_ads,software_development_phantom_ads,web_development_phantom_ads,

        angle_investor_fb_ads,business_angle_fb_ads,pitchdesk_fb_ads,private_investor_fb_ads,venture_capital_fb_ads,angle_investor_lix_ads,fundraising_lix_ads,private_investor_lix_ads,seed_capital_lix_ads,venture_capital_lix_ads,angle_investor_phantom_ads,fundraising_phantom_ads,private_investor_phantom_ads,seed_capital_phantom_ads,venture_capital_phantom_ads,angle_investor_twi_ads,business_angle_twi_ads,fundraising_twi_ads,pitchdesk_twi_ads,private_investor_twi_ads,seed_capital_twi_ads,venture_capital_twi_ads,web3_fund_twi_ads,web3_grants_twi_ads,web3_investor_twi_ads,whitepaper_twi_ads,
        blockchain_fb_ads,blockchain_lix_ads,dao_lix_ads,dapp_lix_ads,defi_lix_ads,nft_lix_ads,yield_farming_lix_ads,blockchain_phantom_ads,dao_phantom_ads,dapp_phantom_ads,defi_phantom_ads,nft_phantom_ads,yield_farming_phantom_ads,defi_twi,defi_twi_ads,

        entrepreneurs_insta_ads,digital_marketing_insta_ads,uiux_insta_ads,micromente_insta_ads,menterpass_insta_ads,graph_list
)

app_name = 'accounts'

urlpatterns = [
    path('log-in/', LogInView.as_view(), name='log_in'),
    path('log-out/', LogOutView.as_view(), name='log_out'),

    path('graph_list/', graph_list, name='graph_list'),

    path('sign-up/', SignUpView.as_view(), name='sign_up'),
   
    path('defi_twi/',defi_twi,name='defi_twi'),
    path('defi_twi_ads/',defi_twi_ads,name='defi_twi_ads'),

    
    path('figma_lix/',figma_lix,name='figma_lix'),
    path('notion_lix/',notion_lix,name='notion_lix'),
    path('slack_lix/',slack_lix,name='slack_lix'),
    path('trello_lix/',trello_lix,name='trello_lix'),
    path('miro_lix/',miro_lix,name='miro_lix'),
    path('micromenter_insta/',micromenter_insta,name='micromenter_insta'),
    path('menterpass_insta/',menterpass_insta,name='menterpass_insta'),
    path('micromenter_twi/',micromenter_twi,name='micromenter_twi'),
    path('menterpass_twi/',menterpass_twi,name='menterpass_twi'),

    path('figma_twi/',figma_twi,name='figma_twi'),
    path('onalytica_twi/',onalytica_twi,name='onalytica_twi'),
    path('slack_twi/',slack_twi,name='slack_twi'),
    path('trello_twi/',trello_twi,name='trello_twi'),
    path('miro_twi/',miro_twi,name='miro_twi'),
    path('notion_twi/',notion_twi,name='notion_twi'),

    path('figma_phantom/',figma_phantom,name='figma_phantom'),
    path('notion_phantom/',notion_phantom,name='notion_phantom'),
    path('slack_phantom/',slack_phantom,name='slack_phantom'),
    path('trello_phantom/',trello_phantom,name='trello_phantom'),
    path('bd_design_lix/',bd_design_lix,name='bd_design_lix'),
    path('bd_design_phantom/',bd_design_phantom,name='bd_design_phantom'),

    path('linkedin_lix/',linkedin_lix,name='linkedin_lix'),
    path('venture_capital_lix/',vc_lix,name='venture_capital_lix'),
    path('angle_investor_lix/',angel_lix,name='angle_investor_lix'),
    path('private_investor_lix/',pi_lix,name='private_investor_lix'),
    path('seed_capital_lix/',sc_lix,name='seed_capital_lix'),
    path('fundraising_lix/',fr_lix,name='fundraising_lix'),
    path('venture_capital_phantom/',vc_phantom,name='venture_capital_phantom'),
    path('angle_investor_phantom/',angel_phantom,name='angle_investor_phantom'),
    path('seed_capital_phantom/',sc_phantom,name='seed_capital_phantom'),
    path('fundraising_phantom/',fr_phantom,name='fundraising_phantom'),
    path('private_investor_phantom/',pi_phantom,name='private_investor_phantom'),

    path('venture_capital_fb/',vc_fb,name='venture_capital_fb'),
    path('angle_investor_fb/',angle_investor_fb_view,name='angle_investor_fb'),
    path('pitchdesk_fb/',pd_fb,name='pitchdesk_fb'),
    path('private_investor_fb/',pi_fb,name='private_investor_fb'),
    path('business_angle_fb/',ba_fb,name='business_angle_fb'),


    path('venture_capital_twi/',vc_twi,name='venture_capital_twi'),
    path('angle_investor_twi/',angeli_twi,name='angle_investor_twi'),
    path('seed_capital_twi/',sc_twi,name='seed_capital_twi'),
    path('web3_fund_twi/',wf_twi,name='web3_fund_twi'),
    path('web3_grants_twi/',wg_twi,name='web3_grants_twi'),
    path('fundraising_twi/',fr_twi,name='fundraising_twi'),
    path('whitepaper_twi/',wp_twi,name='whitepaper_twi'),
    path('pitchdesk_twi/',pd_twi,name='pitchdesk_twi'),
    path('private_investor_twi/',pi_twi,name='private_investor_twi'),
    path('business_angle_twi/',ba_twi,name='business_angle_twi'),
    path('web3_investor_twi/',wi_twi,name='web3_investor_twi'),

    path('digital_marketing_fb/',dmarketing_fb,name='digital_marketing_fb'),
    path('block_fb/',block_fb,name='block_fb'),
    path('sd_fb/',sd_fb,name='sd_fb'),
    path('da_fb/',da_fb,name='da_fb'),
    path('ux_ui_fb/',ux_ui_fb,name='ux_ui_fb'),
    path('enter_fb/',enter_fb,name='enter_fb'),
    path('uiux_instagram/',uiux_instagram,name='uiux_instagram'),
    path('enter_instagram/',enter_instagram,name='enter_instagram'),
    path('dm_instagram/',dm_instagram,name='dm_instagram'),
    path('dmar_twi/',dmar_twi,name='dmar_twi'),
    path('enter_twi/',enter_twi,name='enter_twi'),
    path('uxuidesign_twi/',uxuidesign_twi,name='uxuidesign_twi'),

    path('3d_design_lix/',d3_design_lix,name='3d_design_lix'),
    path('graphic_design_lix/',gd_lix,name='graphic_design_lix'),
    path('visual_design_lix/',vd_lix,name='visual_design_lix'),
    path('marketing_designer_lix/',md_lix,name='marketing_designer_lix'),
    path('branding_consultant_lix/',bc_lix,name='branding_consultant_lix'),


    path('3d_design_phantom/',d3_phantom,name='3d_design_phantom'),
    path('graphic_design_phantom/',gd_phantom,name='graphic_design_phantom'),
    path('visual_design_phantom/',vd_phantom,name='visual_design_phantom'),
    path('marketing_designer_phantom/',md_phantom,name='marketing_designer_phantom'),
    path('branding_consultant_phantom/',bc_phantom,name='branding_consultant_phantom'),

    path('3d_design_twi/',design_twi,name='3d_design_twi'),
    path('graphic_design_twi/',gd_twi,name='graphic_design_twi'),
    path('visual_design_twi/',vd_twi,name='visual_design_twi'),
    path('marketing_designer_twi/',md_twi,name='marketing_designer_twi'),
    path('branding_consultant_twi/',bc_twi,name='branding_consultant_twi'),

    path('3d_design_fb/',d3_fb,name='3d_design_fb'),
    path('graphic_design_fb/',gd_fb,name='graphic_design_fb'),
    

    path('ai_phantom/',ai_phantom,name='ai_phantom'),
    path('ml_phantom/',ml_phantom,name='ml_phantom'),
    path('algo_phantom/',algo_phantom,name='algo_phantom'),
    path('dm_phantom/',dm_phantom,name='dm_phantom'),
    path('ann_phantom/',ann_phantom,name='ann_phantom'),
    path('dp_phantom/',dp_phantom,name='dp_phantom'),

    path('ai_lix/',ai_lix,name='ai_lix'),
    path('ml_lix/',ml_lix,name='ml_lix'),
    path('algo_lix/',algo_lix,name='algo_lix'),
    path('dm_lix/',dm_lix,name='dm_lix'),
    path('ann_lix/',ann_lix,name='ann_lix'),
    path('dp_lix/',dp_lix,name='dp_lix'),

    path('ai_fb/',ai_fb,name='ai_fb'),
    path('ml_fb/',ml_fb,name='ml_fb'),
    path('algo_fb/',algo_fb,name='algo_fb'),
    path('dm_fb/',dm_fb,name='dm_fb'),
    path('ann_fb/',ann_fb,name='ann_fb'),
    
    path('ai_twi/',ai_twi,name='ai_twi'),
    path('ml_twi/',ml_twi,name='ml_twi'),
    path('algo_twi/',algo_twi,name='algo_twi'),
    path('dm_twi/',dm_twi,name='dm_twi'),
    path('ann_twi/',ann_twi,name='ann_twi'),
    path('dp_twi/',dp_twi,name='dp_twi'),

    path('digital_marketing/',digital_marketing,name='digital_marketing'),
    path('blockchain/',blockchain,name='blockchain'),
    path('data_analysis/',data_analysis,name='data_analysis'),
    # path('venture_funding1/',venture_funding,name='venture_funding1'),
    path('uiux/',uiux,name='uiux'),
    path('software/',software,name='software'),
    path('pm_lix/',pm_lix,name='pm_lix'),
    path('software_dev_phantom/',software_dev_phantom,name='software_dev_phantom'),
    path('blockchain_phantom/',blockchain_phantom,name='blockchain_phantom'),
    path('digital_marketing_phantom/',digital_marketing_phantom,name='digital_marketing_phantom'),
    path('data_analysis_phantom/',data_analysis_phantom,name='data_analysis_phantom'),
    # path('venture_funding1_phantom/',venture_funding_phantom,name='venture_funding1_phantom'),
    path('uiux_phantom/',uiux_phantom,name='uiux_phantom'),
    path('pm_phantom/',pm_phantom,name='pm_phantom'),
    path('cb_twi_view/',cb_twi_view,name='cb_twi_view'),
    path('cg_twi_view/',cg_twi_view,name='cg_twi_view'),
    path('cm_twi_view/',cm_twi_view,name='cm_twi_view'),
    path('twi_marketing_view/',twi_marketing_view,name='twi_marketing_view'),
    path('web3_com_twi_view/',web3_com_twi_view,name='web3_com_twi_view'),
    path('web3_marketing_twi_view/',web3_marketing_twi_view,name='web3_marketing_twi_view'),
    path('discordbot_twi_view/',discordbot_twi_view,name='discordbot_twi_view'),
    path('chatbots_twi_view/',chatbots_twi_view,name='chatbots_twi_view'),

    path('linkedin_group/',linkedin_group,name='linkedin_group'),
    path('linkedin_search/',linkedin_search,name='linkedin_search'),
    path('facebook/',facebook,name='facebook'),
    path('twitter/',twitter,name='twitter'),
    path('twitter_web3/',twitter_web3,name='twitter_web3'),
    path('Blank/',Blank,name='Blank'),
    path('wonderverse/',wonderverse,name='wonderverse'),
    path('accelerators/',accelerators,name='accelerators'),
    path('entrepreneurs/',entrepreneurs,name='entrepreneurs'),
    path('founders/',founders,name='founders'),
    path('scaleups/',scaleups,name='scaleups'),
    path('display_count/',display_count,name='display_count'),
    path('data_scientist_phantom/',data_scientist_phantom,name='data_scientist_phantom'),
    path('nft_phantom/',nft_phantom,name='nft_phantom'),
    path('defi_phantom/',defi_phantom,name='defi_phantom'),
    path('dapp_phantom/',dapp_phantom,name='dapp_phantom'),
    path('dao_phantom/',dao_phantom,name='dao_phantom'),
    path('yf_phantom/',yf_phantom,name='yf_phantom'),
    path('data_scientist_lix/',data_scientist_lix,name='data_scientist_lix'),
    path('nft_lix/',nft_lix,name='nft_lix'),
    path('defi_lix/',defi_lix,name='defi_lix'),
    path('dapp_lix/',dapp_lix,name='dapp_lix'),
    path('dao_lix/',dao_lix,name='dao_lix'),
    path('yf_lix/',yf_lix,name='yf_lix'),
    path('web_dev_phantom_display/',web_dev_phantom_display,name='web_dev_phantom_display'),
    path('Web_dev/',Web_dev,name='Web_dev'),
    path('mobile_dev_lix/',mobile_dev_lix,name='mobile_dev_lix'),
    path('mobile_dev_phantom/',mobile_dev_phantom,name='mobile_dev_phantom'),
    path('cm_phantom/',cm_phantom,name='cm_phantom'),
    path('cb_phantom/',cb_phantom,name='cb_phantom'),
    path('cmanag_phantom/',cmanag_phantom,name='cmanag_phantom'),
    path('dc_phantom/',dc_phantom,name='dc_phantom'),

    path('cm_lix/',cm_lix,name='cm_lix'),
    path('cb_lix/',cb_lix,name='cb_lix'),
    path('cmanag_lix/',cmanag_lix,name='cmanag_lix'),
    path('dc_lix/',dc_lix,name='dc_lix'),

    path('entrepreneurs_phantom/',entrepreneurs_phantom,name='entrepreneurs_phantom'),
    path('founders_phantom/',founders_phantom,name='founders_phantom'),

    #AI Ads
    path('algo_fb_ads/',algo_fb_ads,name='algo_fb_ads'),
    path('ai_fb_ads/',ai_fb_ads,name='ai_fb_ads'),
    path('dataanalysis_fb_ads/',dataanalysis_fb_ads,name='dataanalysis_fb_ads'),
    path('dm_fb_ads/',dm_fb_ads,name='dm_fb_ads'),
    path('ml_fb_ads/',ml_fb_ads,name='ml_fb_ads'),
    path('ann_fb_ads/',ann_fb_ads,name='ann_fb_ads'),
    path('algo_lix_ads/',algo_lix_ads,name='algo_lix_ads'),
    path('ai_lix_ads/',ai_lix_ads,name='ai_lix_ads'),
    path('dataanalysis_lix_ads/',dataanalysis_lix_ads,name='dataanalysis_lix_ads'),
    path('dm_lix_ads/',dm_lix_ads,name='dm_lix_ads'),
    path('dp_lix_ads/',dp_lix_ads,name='dp_lix_ads'),
    path('ds_lix_ads/',ds_lix_ads,name='ds_lix_ads'),
    path('ml_lix_ads/',ml_lix_ads,name='ml_lix_ads'),
    path('ann_lix_ads/',ann_lix_ads,name='ann_lix_ads'),
    path('algo_phantom_ads/',algo_phantom_ads,name='algo_phantom_ads'),
    path('ai_phantom_ads/',ai_phantom_ads,name='ai_phantom_ads'),
    path('dataanalysis_phantom_ads/',dataanalysis_phantom_ads,name='dataanalysis_phantom_ads'),
    path('dm_phantom_ads/',dm_phantom_ads,name='dm_phantom_ads'),
    path('dp_phantom_ads/',dp_phantom_ads,name='dp_phantom_ads'),
    path('ds_phantom_ads/',ds_phantom_ads,name='ds_phantom_ads'),
    path('ml_phantom_ads/',ml_phantom_ads,name='ml_phantom_ads'),
    path('ann_phantom_ads/',ann_phantom_ads,name='ann_phantom_ads'),
    path('algo_twi_ads/',algo_twi_ads,name='algo_twi_ads'),
    path('ai_twi_ads/',ai_twi_ads,name='ai_twi_ads'),
    path('dm_twi_ads/',dm_twi_ads,name='dm_twi_ads'),
    path('dp_twi_ads/',dp_twi_ads,name='dp_twi_ads'),
    path('ml_twi_ads/',ml_twi_ads,name='ml_twi_ads'),
    path('ann_twi_ads/',ann_twi_ads,name='ann_twi_ads'),

    #Colloboration tools

    path('figma_lix_ads/',figma_lix_ads,name='figma_lix_ads'),
    #path('miro_lix_ads/',miro_lix_ads,name='miro_lix_ads'),
    path('notion_lix_ads/',notion_lix_ads,name='notion_lix_ads'),
    path('slack_lix_ads/',slack_lix_ads,name='slack_lix_ads'),
    path('trello_lix_ads/',trello_lix_ads,name='trello_lix_ads'),
    path('figma_phantom_ads/',figma_phantom_ads,name='figma_phantom_ads'),
    path('notion_phantom_ads/',notion_phantom_ads,name='notion_phantom_ads'),
    path('slack_phantom_ads/',slack_phantom_ads,name='slack_phantom_ads'),
    path('trello_phantom_ads/',trello_phantom_ads,name='trello_phantom_ads'),
    path('figma_twi_ads/',figma_twi_ads,name='figma_twi_ads'),
    path('miro_twi_ads/',miro_twi_ads,name='miro_twi_ads'),
    path('notion_twi_ads/',notion_twi_ads,name='notion_twi_ads'),
    path('onalytica_twi_ads/',onalytica_twi_ads,name='onalytica_twi_ads'),
    path('slack_twi_ads/',slack_twi_ads,name='slack_twi_ads'),
    path('trello_twi_ads/',trello_twi_ads,name='trello_twi_ads'),
        
    path('cb_lix_ads/',cb_lix_ads,name='cb_lix_ads'),
    path('cmanag_lix_ads/',cmanag_lix_ads,name='cmanag_lix_ads'),
    path('cm_lix_ads/',cm_lix_ads,name='cm_lix_ads'),
    path('dc_lix_ads/',dc_lix_ads,name='dc_lix_ads'),
    path('cb_phantom_ads/',cb_phantom_ads,name='cb_phantom_ads'),
    path('cmanag_phantom_ads/',cmanag_phantom_ads,name='cmanag_phantom_ads'),
    path('cm_phantom_ads/',cm_phantom_ads,name='cm_phantom_ads'),
    path('dc_phantom_ads/',dc_phantom_ads,name='dc_phantom_ads'),
    path('chatbot_twi_ads/',chatbot_twi_ads,name='chatbot_twi_ads'),
    path('cb_twi_ads/',cb_twi_ads,name='cb_twi_ads'),
    path('cg_twi_ads/',cg_twi_ads,name='cg_twi_ads'),
    path('cm_twi_ads/',cm_twi_ads,name='cm_twi_ads'),
    path('db_twi_ads/',db_twi_ads,name='db_twi_ads'),
    path('twi_marketing_twi_ads/',twi_marketing_twi_ads,name='twi_marketing_twi_ads'),
    path('web3_commu_twi_ads/',web3_commu_twi_ads,name='web3_commu_twi_ads'),
    path('web3_marketing_twi_ads/',web3_marketing_twi_ads,name='web3_marketing_twi_ads'),


    path('enterpreneurs_fb_ads/',enterpreneurs_fb_ads,name='enterpreneurs_fb_ads'),
    path('enterpreneurs_lix__ads/',enterpreneurs_lix__ads,name='enterpreneurs_lix__ads'),
    path('founder_lix_ads/',founder_lix_ads,name='founder_lix_ads'),
    path('enterpreneurs_phantom_ads/',enterpreneurs_phantom_ads,name='enterpreneurs_phantom_ads'),
    path('founders_phantom_ads/',founders_phantom_ads,name='founders_phantom_ads'),
    path('enterpreneurs_twi_ads/',enterpreneurs_twi_ads,name='enterpreneurs_twi_ads'),
    
    
    path('d3_design_fb_ads/',d3_design_fb_ads,name='d3_design_fb_ads'),
    path('graphic_design_fb_ads/',graphic_design_fb_ads,name='graphic_design_fb_ads'),
    path('uiux_design_fb_ads/',uiux_design_fb_ads,name='uiux_design_fb_ads'),
    path('d3_design_lix_ads/',d3_design_lix_ads,name='d3_design_lix_ads'),
    path('brand_designers_lix_ads/',brand_designers_lix_ads,name='brand_designers_lix_ads'),
    path('branding_consultant_lix_ads/',branding_consultant_lix_ads,name='branding_consultant_lix_ads'),
    path('graphic_design_lix_ads/',graphic_design_lix_ads,name='graphic_design_lix_ads'),
    path('marketing_designer_lix_ads/',marketing_designer_lix_ads,name='marketing_designer_lix_ads'),
    path('uiux_lix_ads/',uiux_lix_ads,name='uiux_lix_ads'),
    path('visual_design_lix_ads/',visual_design_lix_ads,name='visual_design_lix_ads'),
    path('d3_design_phantom_ads/',d3_design_phantom_ads,name='d3_design_phantom_ads'),
    path('brand_designers_phantom_ads/',brand_designers_phantom_ads,name='brand_designers_phantom_ads'),
    path('branding_consultant_phantom_ads/',branding_consultant_phantom_ads,name='branding_consultant_phantom_ads'),
    path('graphic_design_phantom_ads/',graphic_design_phantom_ads,name='graphic_design_phantom_ads'),
    path('marketing_designer_phantom_ads/',marketing_designer_phantom_ads,name='marketing_designer_phantom_ads'),
    path('uiux_design_phantom_ads/',uiux_design_phantom_ads,name='uiux_design_phantom_ads'),
    path('visual_design_phantom_ads/',visual_design_phantom_ads,name='visual_design_phantom_ads'),
    path('d3_design_twi_ads/',d3_design_twi_ads,name='d3_design_twi_ads'),
    path('branding_consultant_twi_ads/',branding_consultant_twi_ads,name='branding_consultant_twi_ads'),
    path('graphic_design_twi_ads/',graphic_design_twi_ads,name='graphic_design_twi_ads'),
    path('marketing_designer_twi_ads/',marketing_designer_twi_ads,name='marketing_designer_twi_ads'),
    path('uiux_design_twi_ads/',uiux_design_twi_ads,name='uiux_design_twi_ads'),
    path('visual_design_twi_ads/',visual_design_twi_ads,name='visual_design_twi_ads'),

    path('micromentor_twi_ads/',micromentor_twi_ads,name='micromentor_twi_ads'),
    path('mentorpass_twi_ads/',mentorpass_twi_ads,name='mentorpass_twi_ads'),

    path('digital_marketing_fb_ads/',digital_marketing_fb_ads,name='digital_marketing_fb_ads'),
    path('digital_marketing_lix_ads/',digital_marketing_lix_ads,name='digital_marketing_lix_ads'),
    path('digital_marketing_phantom_ads/',digital_marketing_phantom_ads,name='digital_marketing_phantom_ads'),
    path('digital_marketing_twi_ads/',digital_marketing_twi_ads,name='digital_marketing_twi_ads'),

    path('pm_fit_lix_ads/',pm_fit_lix_ads,name='pm_fit_lix_ads'),
    path('pm_fit_phantom_ads/',pm_fit_phantom_ads,name='pm_fit_phantom_ads'),

    path('software_development_fb_ads/',software_development_fb_ads,name='software_development_fb_ads'),
    path('mobile_development_lix_ads/',mobile_development_lix_ads,name='mobile_development_lix_ads'),
    path('software_development_lix_ads/',software_development_lix_ads,name='software_development_lix_ads'),
    path('web_development_lix_ads/',web_development_lix_ads,name='web_development_lix_ads'),
    path('mobile_development_phantom_ads/',mobile_development_phantom_ads,name='mobile_development_phantom_ads'),
    path('software_development_phantom_ads/',software_development_phantom_ads,name='software_development_phantom_ads'),
    path('web_development_phantom_ads/',web_development_phantom_ads,name='web_development_phantom_ads'),

    path('angle_investor_fb_ads/',angle_investor_fb_ads,name='angle_investor_fb_ads'),
    path('business_angle_fb_ads/',business_angle_fb_ads,name='business_angle_fb_ads'),
    path('pitchdesk_fb_ads/',pitchdesk_fb_ads,name='pitchdesk_fb_ads'),
    path('private_investor_fb_ads/',private_investor_fb_ads,name='private_investor_fb_ads'),
    path('venture_capital_fb_ads/',venture_capital_fb_ads,name='venture_capital_fb_ads'),
    path('angle_investor_lix_ads/',angle_investor_lix_ads,name='angle_investor_lix_ads'),
    path('fundraising_lix_ads/',fundraising_lix_ads,name='fundraising_lix_ads'),
    path('private_investor_lix_ads/',private_investor_lix_ads,name='private_investor_lix_ads'),
    path('seed_capital_lix_ads/',seed_capital_lix_ads,name='seed_capital_lix_ads'),
    path('venture_capital_lix_ads/',venture_capital_lix_ads,name='venture_capital_lix_ads'),
    path('angle_investor_phantom_ads/',angle_investor_phantom_ads,name='angle_investor_phantom_ads'),
    path('fundraising_phantom_ads/',fundraising_phantom_ads,name='fundraising_phantom_ads'),
    path('private_investor_phantom_ads/',private_investor_phantom_ads,name='private_investor_phantom_ads'),
    path('seed_capital_phantom_ads/',seed_capital_phantom_ads,name='seed_capital_phantom_ads'),
    path('venture_capital_phantom_ads/',venture_capital_phantom_ads,name='venture_capital_phantom_ads'),
    path('angle_investor_twi_ads/',angle_investor_twi_ads,name='angle_investor_twi_ads'),
    path('business_angle_twi_ads/',business_angle_twi_ads,name='business_angle_twi_ads'),
    path('fundraising_twi_ads/',fundraising_twi_ads,name='fundraising_twi_ads'),
    path('pitchdesk_twi_ads/',pitchdesk_twi_ads,name='pitchdesk_twi_ads'),
    path('private_investor_twi_ads/',private_investor_twi_ads,name='private_investor_twi_ads'),
    path('seed_capital_twi_ads/',seed_capital_twi_ads,name='seed_capital_twi_ads'),
    path('venture_capital_twi_ads/',venture_capital_twi_ads,name='venture_capital_twi_ads'),
    path('web3_fund_twi_ads/',web3_fund_twi_ads,name='web3_fund_twi_ads'),
    path('web3_grants_twi_ads/',web3_grants_twi_ads,name='web3_grants_twi_ads'),
    path('web3_investor_twi_ads/',web3_investor_twi_ads,name='web3_investor_twi_ads'),
    path('whitepaper_twi_ads/',whitepaper_twi_ads,name='whitepaper_twi_ads'),

    path('blockchain_fb_ads/',blockchain_fb_ads,name='blockchain_fb_ads'),
    path('blockchain_lix_ads/',blockchain_lix_ads,name='blockchain_lix_ads'),
    path('dao_lix_ads/',dao_lix_ads,name='dao_lix_ads'),
    path('dapp_lix_ads/',dapp_lix_ads,name='dapp_lix_ads'),
    path('defi_lix_ads/',defi_lix_ads,name='defi_lix_ads'),
    path('nft_lix_ads/',nft_lix_ads,name='nft_lix_ads'),
    path('yield_farming_lix_ads/',yield_farming_lix_ads,name='yield_farming_lix_ads'),
    path('blockchain_phantom_ads/',blockchain_phantom_ads,name='blockchain_phantom_ads'),
    path('dao_phantom_ads/',dao_phantom_ads,name='dao_phantom_ads'),
    path('dapp_phantom_ads/',dapp_phantom_ads,name='dapp_phantom_ads'),
    path('defi_phantom_ads/',defi_phantom_ads,name='defi_phantom_ads'),
    path('nft_phantom_ads/',nft_phantom_ads,name='nft_phantom_ads'),
    path('yield_farming_phantom_ads/',yield_farming_phantom_ads,name='yield_farming_phantom_ads'),

    path('entrepreneurs_insta_ads/',entrepreneurs_insta_ads,name='entrepreneurs_insta_ads'),
    path('digital_marketing_insta_ads/',digital_marketing_insta_ads,name='digital_marketing_insta_ads'),
    path('uiux_insta_ads/',uiux_insta_ads,name='uiux_insta_ads'),
    path('micromente_insta_ads/',micromente_insta_ads,name='micromente_insta_ads'),
    path('menterpass_insta_ads/',menterpass_insta_ads,name='menterpass_insta_ads'),


]