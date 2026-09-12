# File: moyee_account_page_19/models/res_config_settings.py
from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    moyee_enable_company_portal = fields.Boolean(
        string="Enable Moyee Account Page Portal",
        default=True,
        help="If checked, the custom Moyee account portal page (/my/home) will be active for this company.",
    )
    moyee_enable_company_filter = fields.Boolean(
        string="Filter Redesign Portal by Specific Companies",
        default=False,
        help="If checked, only the selected companies will display the custom Moyee Account Page portal.",
    )
    moyee_allowed_company_ids = fields.Many2many(
        comodel_name="res.company",
        relation="moyee_company_allowed_rel",
        column1="company_id",
        column2="allowed_company_id",
        string="Allowed Companies for Portal Redesign",
        help="Select companies where the redesign portal should be enabled.",
    )
    moyee_enable_user_filter = fields.Boolean(
        string="Filter New Portal Home Page by Specific Subscription Customers",
        default=False,
        help="If checked, only the selected subscription customers will see the new Moyee Portal Home page (/my/home). Unselected users will see Odoo's default portal page.",
    )
    moyee_redesign_partner_ids = fields.Many2many(
        comodel_name="res.partner",
        relation="moyee_company_redesign_partner_rel",
        column1="company_id",
        column2="partner_id",
        string="Selected Subscription Customers",
        help="Select subscription customers/partners who will see the new Moyee Portal Home page (/my/home). Unselected users will see Odoo's default portal page.",
    )


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    moyee_enable_company_portal = fields.Boolean(
        related="company_id.moyee_enable_company_portal",
        readonly=False,
        string="Enable Moyee Account Page Portal for Active Company",
    )
    moyee_enable_company_filter = fields.Boolean(
        related="company_id.moyee_enable_company_filter",
        readonly=False,
        string="Filter Redesign Portal by Specific Companies",
    )
    moyee_allowed_company_ids = fields.Many2many(
        related="company_id.moyee_allowed_company_ids",
        readonly=False,
        string="Allowed Companies for Portal Redesign",
    )
    moyee_enable_user_filter = fields.Boolean(
        related="company_id.moyee_enable_user_filter",
        readonly=False,
        string="Filter New Portal Home Page by Specific Subscription Customers",
    )
    moyee_redesign_partner_ids = fields.Many2many(
        related="company_id.moyee_redesign_partner_ids",
        readonly=False,
        string="Selected Subscription Customers",
    )

    # Styling Overrides
    moyee_primary_color = fields.Char(
        string="Primary Color",
        config_parameter="moyee_account_page_19.primary_color",
        default="#E91E8C",
    )
    moyee_secondary_color = fields.Char(
        string="Secondary Color (Light Accent)",
        config_parameter="moyee_account_page_19.secondary_color",
        default="#FCE4F3",
    )
    moyee_font_family = fields.Selection(
        [
            ("Inter", "Inter"),
            ("Roboto", "Roboto"),
            ("Outfit", "Outfit"),
            ("Montserrat", "Montserrat"),
            ("Open Sans", "Open Sans"),
            ("system-ui", "System Default"),
        ],
        string="Font Family",
        config_parameter="moyee_account_page_19.font_family",
        default="system-ui",
    )

    # Visibility Controls
    moyee_show_subscription = fields.Boolean(
        string="Show Subscription Section",
        config_parameter="moyee_account_page_19.show_subscription",
    )
    moyee_show_overview = fields.Boolean(
        string="Show Overview Section",
        config_parameter="moyee_account_page_19.show_overview",
    )
    moyee_show_orders = fields.Boolean(
        string="Show Orders Section",
        config_parameter="moyee_account_page_19.show_orders",
    )
    moyee_show_invoices = fields.Boolean(
        string="Show Invoices Section",
        config_parameter="moyee_account_page_19.show_invoices",
    )
    moyee_show_faq = fields.Boolean(
        string="Show FAQ Section",
        config_parameter="moyee_account_page_19.show_faq",
    )
    moyee_show_inspire = fields.Boolean(
        string="Show Inspire Section",
        config_parameter="moyee_account_page_19.show_inspire",
    )
    moyee_show_taf = fields.Boolean(
        string="Show Tell a Friend Card",
        config_parameter="moyee_account_page_19.show_taf",
    )
    moyee_show_brew_guides = fields.Boolean(
        string="Show Brew Guides Section",
        config_parameter="moyee_account_page_19.show_brew_guides",
    )

    # Sidebar Visibility Controls
    moyee_show_sidebar_profile = fields.Boolean(
        string="Show Profile Card",
        config_parameter="moyee_account_page_19.show_sidebar_profile",
    )
    moyee_show_sidebar_upsell = fields.Boolean(
        string="Show Upsell Card (Non-Subscribers)",
        config_parameter="moyee_account_page_19.show_sidebar_upsell",
    )
    moyee_show_sidebar_support = fields.Boolean(
        string="Show Support Card",
        config_parameter="moyee_account_page_19.show_sidebar_support",
    )

    # Content Overrides
    moyee_upsell_cta_url = fields.Char(
        string="Upsell CTA URL",
        config_parameter="moyee_account_page_19.upsell_cta_url",
        default="/shop",
    )
    moyee_brew_guides_all_url = fields.Char(
        string="All Brew Guides URL",
        config_parameter="moyee_account_page_19.brew_guides_all_url",
        default="/shop",
    )
    moyee_support_email = fields.Char(
        string="Support Email",
        config_parameter="moyee_account_page_19.support_email",
        default="hello@moyeecoffee.com",
    )

    # Inspire Content Overrides
    moyee_inspire_eyebrow = fields.Char(
        string="Inspire Section Eyebrow",
        config_parameter="moyee_account_page_19.inspire_eyebrow",
        default="Do you know where your coffee comes from?",
    )
    moyee_inspire_title = fields.Char(
        string="Inspire Section Title",
        config_parameter="moyee_account_page_19.inspire_title",
        default="Your coffee comes from Ethiopia",
    )
    moyee_inspire_body = fields.Char(
        string="Inspire Section Body",
        config_parameter="moyee_account_page_19.inspire_body",
        default="Your Moyee coffee comes from small farmers in the Kaffa forest in Ethiopia. They receive a fair price — thanks to you.",
    )
    moyee_inspire_btn1_text = fields.Char(
        string="Inspire Section Button 1 Text",
        config_parameter="moyee_account_page_19.inspire_btn1_text",
        default="Read the story",
    )
    moyee_inspire_btn1_url = fields.Char(
        string="Inspire Section Button 1 URL",
        config_parameter="moyee_account_page_19.inspire_btn1_url",
        default="/radical-impact-coffee",
    )
    moyee_inspire_btn2_text = fields.Char(
        string="Inspire Section Button 2 Text",
        config_parameter="moyee_account_page_19.inspire_btn2_text",
        default="Browse our coffee",
    )
    moyee_inspire_btn2_url = fields.Char(
        string="Inspire Section Button 2 URL",
        config_parameter="moyee_account_page_19.inspire_btn2_url",
        default="/shop",
    )

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        ICP = self.env["ir.config_parameter"].sudo()

        def _param(key, default="True"):
            val = ICP.get_param(f"moyee_account_page_19.{key}")
            if val is None:
                val = ICP.get_param(f"moyee_subscription_portal_manager.{key}", default)
            return str(val).lower() in ("true", "1", "yes")

        res.update(
            moyee_show_subscription=_param("show_subscription"),
            moyee_show_overview=_param("show_overview"),
            moyee_show_orders=_param("show_orders"),
            moyee_show_invoices=_param("show_invoices"),
            moyee_show_faq=_param("show_faq"),
            moyee_show_inspire=_param("show_inspire"),
            moyee_show_taf=_param("show_taf"),
            moyee_show_brew_guides=_param("show_brew_guides"),
            moyee_show_sidebar_profile=_param("show_sidebar_profile"),
            moyee_show_sidebar_upsell=_param("show_sidebar_upsell"),
            moyee_show_sidebar_support=_param("show_sidebar_support"),
        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        ICP = self.env["ir.config_parameter"].sudo()
        params = {
            "show_subscription": str(self.moyee_show_subscription),
            "show_overview": str(self.moyee_show_overview),
            "show_orders": str(self.moyee_show_orders),
            "show_invoices": str(self.moyee_show_invoices),
            "show_faq": str(self.moyee_show_faq),
            "show_inspire": str(self.moyee_show_inspire),
            "show_taf": str(self.moyee_show_taf),
            "show_brew_guides": str(self.moyee_show_brew_guides),
            "show_sidebar_profile": str(self.moyee_show_sidebar_profile),
            "show_sidebar_upsell": str(self.moyee_show_sidebar_upsell),
            "show_sidebar_support": str(self.moyee_show_sidebar_support),
        }
        for key, val in params.items():
            ICP.set_param(f"moyee_account_page_19.{key}", val)
            ICP.set_param(f"moyee_subscription_portal_manager.{key}", val)

