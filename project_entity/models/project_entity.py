# -*- coding: utf-8 -*-
##############################################################################
#   Entity for projects
##############################################################################
from openerp import models, fields, api
from openerp import tools


class ProjectProjectEntity(models.Model):
    _inherit = 'project.project'

    entity_id = fields.Many2one('project.entity', 'Entity')


class ProjectEntity(models.Model):
    _name = 'project.entity'
    _description = 'Entity'

    name = fields.Char('Name', required=True, select=True)
    comment = fields.Text('Notes')
    active = fields.Boolean('Active', default=True)
    street = fields.Char('Street')
    street2 = fields.Char('Street2')
    zip = fields.Char('Zip', size=24, change_default=True)
    city = fields.Char('City')
    state_id = fields.Many2one('res.country.state', 'State', ondelete='restrict')
    country_id = fields.Many2one('res.country', 'Country', ondelete='restrict')
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    fax = fields.Char('Fax')
    company_id = fields.Many2one('res.company', 'Company', select=1)

    project_ids = fields.One2many('project.project', 'entity_id')

    image = fields.Binary('Image', attachment=True)

    image_medium = fields.Binary(string="Medium-sized image",
                                 attachment=True,
                                 compute="_get_image",
                                 help="Medium-sized image of this model. It is automatically " \
                                      "resized as a 128x128px image, with aspect ratio preserved. " \
                                      "Use this field in form views or some kanban views.")

    image_small = fields.Binary(string="Small-sized image",
                                attachment=True,
                                compute="_get_image",
                                help="Small sized image of this model. It is automatically " \
                                     "resized as a 64x64px image, with aspect ratio preserved. " \
                                     "Use this field in form views or some kanban views.")\

    @api.one
    @api.depends("image")
    def _get_image(self):
        """ calculate the images sizes and set the images to the corresponding fields
        """
        image = self.image

        data = tools.image_get_resized_images(image)
        self.image_medium = data["image_medium"]
        self.image_small = data["image_small"]
        return True

    @api.multi
    def onchange_state(self, state_id):
        if state_id:
            state = self.env['res.country.state'].browse(state_id)
            return {'value': {'country_id': state.country_id.id}}
        return {'value': {}}

