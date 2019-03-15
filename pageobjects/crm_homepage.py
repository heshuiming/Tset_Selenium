import time
from unit.base_page import BasePage

class CrmHomePage(BasePage):
    #环球工作台登录页面
    input_username = "id=>login-userName"
    input_pwd = "id=>login-pwd"
    login_sumbit_btn = "id=>submit"
    def login(self,name,password):
        self.send_keys(self.input_username,name) #输入用户名
        self.send_keys(self.input_pwd,password) #输入密码
        self.click(self.login_sumbit_btn) #点击登录
        time.sleep(1)
        self.click(self.crm_logo) #跳转至青龙
        time.sleep(1)
        search_window = self.driver.current_window_handle
        time.sleep(2)
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != search_window:
                self.driver.switch_to.window(handle)
                time.sleep(2)


    # 点击登录按钮
    def login_btn(self):
        self.click(self.login_sumbit_btn)

    # 跳转至青龙系统
    crm_logo = "xpath=>//span[contains(text(),'青龙')]"
    def skip_crm(self):
        self.click(self.crm_logo)

    #“我的资源”模块
    my_source_btn = "xpath=>//span[contains(text(),'我的资源')]"
    #已成学员
    alreadyStudent_btn = "link_text=>已成学员"
    def alreadyStudent(self):  #跳转至我的学员
        self.click(self.my_source_btn)
        time.sleep(2)
        self.click(self.alreadyStudent_btn)

    #待跟进
    followup_btn = "link_text=>待跟进"
    def FollwUp(self):
        self.click(self.my_source_btn)
        time.sleep(2)
        self.click(self.followup_btn)

    #我的到访
    myInvite_btn = "link_text=>我的到访"
    def MyInvite(self):
        self.click(self.my_source_btn)
        time.sleep(2)
        self.click(self.myInvite_btn)

    #我的回访
    myNextInvite_btn = "link_text=>我的回访"
    def MyNextInvite(self):
        self.click(self.my_source_btn)
        time.sleep(2)
        self.click(self.myNextInvite_btn)

    #转出资源
    myInvalidList_btn = "link_text=>转出资源"
    def MyInvalidList(self):
        self.click(self.my_source_btn)
        time.sleep(2)
        self.click(self.myInvalidList_btn)

    #我的资源合并历史
    myResourceMerge_btn = "link_text=>我的资源合并历史"
    def MyResourceMerge(self):
        self.click(self.my_source_btn)
        time.sleep(2)
        self.click(self.myResourceMerge_btn)


    #“资源录入”模块
    resource_input_btn = "xpath=>//span[contains(text(),'资源录入')]"
    #我的口碑资源
    publicPraiseResourceList_btn = "link_text=>我的口碑资源"
    def PublicPraiseResourceList(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.publicPraiseResourceList_btn)

    #我的活动资源
    marketActivityResource_btn = "link_text=>我的活动资源"
    def MarketActivityResource(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.marketActivityResource_btn)

    #活动资源导入历史
    marketActivityImportHistory_btn = "link_text=>活动资源导入历史"
    def MarketActivityImportHistory(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.marketActivityImportHistory_btn)

    #活动管理
    marketActivityManager_btn = "link_text=>活动管理"
    def MarketActivityManager(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.marketActivityManager_btn)

    #我的代理资源
    agentResource_btn = "link_text=>我的代理资源"
    def AgentResource(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.agentResource_btn)

    #代理资源导入历史
    agentImportHistory_btn = "link_text=>代理资源导入历史"
    def AgentImportHistory(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.agentImportHistory_btn)

    #代理管理
    agentManager_btn = "link_text=>代理管理"
    def AgentManager(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.agentManager_btn)

    #我的新媒体资源
    newMediaResource_btn = "link_text=>我的新媒体资源"
    def NewMediaResource(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.newMediaResource_btn)

    #我的TMK资源
    tmkResourceInMy_btn = "link_text=>我的TMK资源"
    def TmkResourceInMy(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.tmkResourceInMy_btn)

    #TMK资源导入历史
    tmkImportHistory_btn = "link_text=>TMK资源导入历史"
    def TmkImportHistory(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.tmkImportHistory_btn)

    #TMK任务设置
    tmkTaskSetting_btn = "link_text=>TMK任务设置"
    def TmkTaskSetting(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.tmkTaskSetting_btn)

    #TMK任务历史查询
    tmkTaskQuery_btn = "link_text=>TMK任务历史查询"
    def TmkTaskQuery(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.tmkTaskQuery_btn)

    #TMK兼职管理
    tmkEmployee_btn = "link_text=>TMK兼职管理"
    def TmkEmployee(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.tmkEmployee_btn)

    #我的客服资源
    customerResource_btn = "link_text=>我的客服资源"
    def CustomerResource(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.customerResource_btn)

    #新增客服资源
    customerResAdd_btn = "link_text=>新增客服资源"
    def CustomerResAdd(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.customerResAdd_btn)

    #我的代理管理
    myAgent_btn = "link_text=>我的代理管理"
    def MyAgent(self):
        self.click(self.resource_input_btn)
        time.sleep(2)
        self.click(self.myAgent_btn)


    #“市场资源”模块
    market_resource_btn = "xpath=>//span[contains(text(),'市场资源')]"
    #全部资源
    allResourceInMarket_btn = "link_text=>全部资源"
    def AllResourceInMarket(self):
        self.click(self.market_resource_btn)
        time.sleep(2)
        self.click(self.allResourceInMarket_btn)

    #全部口碑资源
    allPublicPraiseResourceList_btn = "link_text=>全部口碑资源"
    def AllPublicPraiseResourceList(self):
        self.click(self.market_resource_btn)
        time.sleep(2)
        self.click(self.allPublicPraiseResourceList_btn)

    #全部活动资源
    marketActivityResourceAll_btn = "link_text=>全部活动资源"
    def MarketActivityResourceAll(self):
        self.click(self.market_resource_btn)
        time.sleep(2)
        self.click(self.marketActivityResourceAll_btn)

    #全部代理资源
    agentResourceAll_btn = "link_text=>全部代理资源"
    def AgentResourceAll(self):
        self.click(self.market_resource_btn)
        time.sleep(2)
        self.click(self.agentResourceAll_btn)

    #全部新媒体资源
    newMediaResourceAll_btn = "link_text=>全部新媒体资源"
    def NewMediaResourceAll(self):
        self.click(self.market_resource_btn)
        time.sleep(2)
        self.click(self.newMediaResourceAll_btn)

    #全部TMK资源
    tmkResource_btn = "link_text=>全部TMK资源"
    def TmkResource(self):
        self.click(self.market_resource_btn)
        time.sleep(2)
        self.click(self.tmkResource_btn)

    #全部客服资源
    customerResourceAll_btn = "link_text=>全部客服资源"
    def CustomerResourceAll(self):
        self.click(self.market_resource_btn)
        time.sleep(2)
        self.click(self.customerResourceAll_btn)

    #全部搜课资源
    searchResourceAll_btn = "link_text=>全部搜课资源"
    def SearchResourceAll(self):
        self.click(self.market_resource_btn)
        time.sleep(2)
        self.click(self.searchResourceAll_btn)

    #“资源分配”模块
    resource_allocation_btn = "xpath=>//span[contains(text(),'资源分配')]"
    #全部资源
    onListAllResourceAllocation_btn = "link_text=>全部资源"
    def OnListAllResourceAllocation(self):
        self.click(self.resource_allocation_btn)
        time.sleep(2)
        self.click(self.onListAllResourceAllocation_btn)

    #搜课资源
    searchResourceAllocationList_btn = "link_text=>搜课资源"
    def SearchResourceAllocationList(self):
        self.click(self.resource_allocation_btn)
        time.sleep(2)
        self.click(self.searchResourceAllocationList_btn)

    #代理资源
    agentResourceAllocation_btn = "link_text=>代理资源"
    def AgentResourceAllocation(self):
        self.click(self.resource_allocation_btn)
        time.sleep(2)
        self.click(self.agentResourceAllocation_btn)

    #活动资源
    marketActivityResourceAllocation_btn = "link_text=>活动资源"
    def MarketActivityResourceAllocation(self):
        self.click(self.resource_allocation_btn)
        time.sleep(2)
        self.click(self.marketActivityResourceAllocation_btn)

    #新媒体资源
    newMediaResourceAllocation_btn = "link_text=>新媒体资源"
    def NewMediaResourceAllocation(self):
        self.click(self.resource_allocation_btn)
        time.sleep(2)
        self.click(self.newMediaResourceAllocation_btn)

    #口碑资源
    publicPraisResourceAllocation_btn = "link_text=>口碑资源"
    def PublicPraisResourceAllocation(self):
        self.click(self.resource_allocation_btn)
        time.sleep(2)
        self.click(self.publicPraisResourceAllocation_btn)

    #TMK资源
    tmkResourceAllocation_btn = "link_text=>TMK资源"
    def TmkResourceAllocation(self):
        self.click(self.resource_allocation_btn)
        time.sleep(2)
        self.click(self.tmkResourceAllocation_btn)

    #销售报备资源
    saleResourceAllocation_btn = "link_text=>销售报备资源"
    def SaleResourceAllocation(self):
        self.click(self.resource_allocation_btn)
        time.sleep(2)
        self.click(self.saleResourceAllocation_btn)

    #客服资源
    customerResourceAllocation_btn = "link_text=>客服资源"
    def CustomerResourceAllocation(self):
        self.click(self.resource_allocation_btn)
        time.sleep(2)
        self.click(self.customerResourceAllocation_btn)


    #“资源管理”模块
    resource_manage_btn = "xpath=>//span[contains(text(),'资源管理')]"
    #重复用户管理
    searchResourceMerge_btn = "link_text=>重复用户管理"
    def SearchResourceMerge(self):
        self.click(self.resource_manage_btn)
        time.sleep(2)
        self.click(self.searchResourceMerge_btn)

    #全部资源
    allResource_btn = "link_text=>全部资源"
    def AllResource(self):
        self.click(self.resource_manage_btn)
        time.sleep(2)
        self.click(self.allResource_btn)

    #本组资源
    groupResourceList_btn = "link_text=>本组资源"
    def GroupResourceList(self):
        self.click(self.resource_manage_btn)
        time.sleep(2)
        self.click(self.groupResourceList_btn)

    #全部到访
    allInvite_btn = "link_text=>全部到访"
    def AllInvite(self):
        self.click(self.resource_manage_btn)
        time.sleep(2)
        self.click(self.allInvite_btn)

    #全部回访
    nextVisit_btn = "link_text=>全部回访"
    def NextVisit(self):
        self.click(self.resource_manage_btn)
        time.sleep(2)
        self.click(self.nextVisit_btn)

    #过期资源池
    resourceOverdueClaimList_btn = "link_text=>过期资源池"
    def ResourceOverdueClaimList(self):
        self.click(self.resource_manage_btn)
        time.sleep(2)
        self.click(self.resourceOverdueClaimList_btn)

    #公共资源池
    resourceInvalidClaimList_btn = "link_text=>公共资源池"
    def resourceInvalidClaimList(self):
        self.click(self.resource_manage_btn)
        time.sleep(2)
        self.click(self.resourceInvalidClaimList_btn)

    #全部资源合并历史
    #无效资源池
    #过期资源池管理
    #公共资源池管理
    #再分配
    #组内再分配
    #资源搜索
    #超期资源
