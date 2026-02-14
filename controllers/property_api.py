import json
from odoo import http
from odoo.http import request

class PropertyApi(http.Controller):
    
    @http.route('/v1/property', methods=['POST'], type='http', auth='none', csrf=False)
    def post_property(self):
        try:
            vals = json.loads(request.httprequest.data.decode())
            property_rec = request.env['estate.property'].sudo().create(vals)
            return request.make_json_response({
                'message': 'Property created successfully',
                'id': property_rec.id,
            }, status=201)
        except Exception as error:
            return request.make_json_response({
                'message': str(error),
            }, status=400)


    @http.route('/v1/property/<int:property_id>', methods=['PUT'], type='http', auth='none', csrf=False)
    def update_property(self, property_id):
        try:    
            property_rec = request.env['estate.property'].sudo().browse(property_id)
            if not property_rec.exists():
                return request.make_json_response({
                    'message': 'Property ID not found',
                }, status=404)
            
            vals = json.loads(request.httprequest.data.decode())
            property_rec.write(vals)
            return request.make_json_response({
                'message': 'Property updated successfully',
                'id': property_rec.id,
                'name': property_rec.name,
                }, status=200)
        except Exception as error:
            return request.make_json_response({
                'message': str(error),
            }, status=400)


    @http.route('/v1/property/show', methods=['GET'], type='http', auth='none', csrf=False)
    def get_properties(self):
        try:    
            model = request.env['estate.property'].sudo()
            records = model.search([])

            data = []
            for rec in records:
                data.append({
                    'id': rec.id,
                    'name': rec.name,
                    'description': rec.description,
                })
            return request.make_json_response({
                'count': len(data),
                'results': data,
            }, status=200)
        except Exception as error:
            return request.make_json_response({
                'message': str(error),
            }, status=400)
    
    @http.route('/v1/property/show/<int:property_id>', methods=['GET'], type='http', auth='none', csrf=False)
    def get_property(self, property_id):
        try:
            property_rec = request.env['estate.property'].sudo().browse(property_id)
            if not property_rec.exists():
                return request.make_json_response({
                    'message': 'Property ID not found',
                }, status=404)
            return request.make_json_response({
                'id': property_rec.id,
                'name': property_rec.name,
                'description': property_rec.description,
            }, status=200)
        except Exception as error:
            return request.make_json_response({
                'message': str(error),
            }, status=400)
        
    @http.route('/v1/property/delete/<int:property_id>', methods=['DELETE'], type='http', auth='none', csrf=False)
    def delete_property(self, property_id):
        try:
            property_rec = request.env['estate.property'].sudo().browse(property_id)
            if not property_rec.exists():
                return request.make_json_response({
                    'message': 'Property ID not found',
                }, status=404)
            property_rec.unlink()
            return request.make_json_response({
                'message': 'Property deleted successfully',
            }, status=200)
        except Exception as error:
            return request.make_json_response({
                'message': str(error),
            }, status=400)