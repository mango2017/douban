from django.contrib import admin

# Register your models here.

from TestModel.models import Test,Contact,Tag

# admin.site.register([Test,Contact,Tag])


# class ContactAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ['Main',{
#             'fields':('name','email'),
#         }],
#         ['Advance',{
#             'classes':('collapse',),# CSS
#             'fields':('age',),
#         }]
#     )
#     # fields = ('name','email')
#
# admin.site.register(Contact,ContactAdmin)
# admin.site.register([Test,Tag])

# class TagInline(admin.TabularInline):
#     model = Tag
#
# class ContactAdmin(admin.ModelAdmin):
#     inlines = [TagInline]
#     fieldsets = (
#         ['Main',{
#             'fields':('name','email'),
#         }],
#         ['Advance',{
#             'classes':('collapse',),# CSS
#             'fields':('age',),
#         }]
#     )
#     # fields = ('name','email')
#
# admin.site.register(Contact,ContactAdmin)
# admin.site.register([Test,Tag])


class TagInline(admin.TabularInline):
    model = Tag


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')  # list
    search_fields = ('name',)
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('age',),
        }]

    )


admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])