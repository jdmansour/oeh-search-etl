import scrapy
from scrapy.spiders import CrawlSpider

from converter.constants import Constants
from converter.items import BaseItemLoader, LomBaseItemloader, LomGeneralItemloader, LomTechnicalItemLoader, \
    LomLifecycleItemloader, LomEducationalItemLoader, ValuespaceItemLoader, LicenseItemLoader, ResponseItemLoader, \
    PermissionItemLoader
from converter.spiders.base_classes import LomBase


# This is an alternative approach to our previous "sample_spider.py" that might be easier to read and understand
# for web crawling beginners. Use whichever approach is more convenient for you.
# LAST UPDATE: 2021-08-20
# please also consult converter/items.py for all currently available keys/values in our crawler data model
class SampleSpiderAlternative(CrawlSpider, LomBase):
    name = "sample_spider_alternative"
    friendlyName = "Sample Source (alternative Method)"  # how your crawler should appear in the "Supplier"-list
    start_urls = ["https://edu-sharing.com"]  # starting point of your crawler, e.g. a sitemap, index, rss-feed etc.
    version = "0.0.1"  # this is used for timestamping your crawler results (if a source changes its layout/data,
    # make sure to increment this value to force a clear distinction between old and new crawler results)

    def getId(self, response=None) -> str:
        # You have two choices here:
        # - either implement this method and return the current url of a material as a string
        # - or look into the parse()-method for base.add_value('sourceId', response.url) is set manually
        pass

    def getHash(self, response=None) -> str:
        # The hash should always be unique, e.g. by string-concatenating using the publicationDate + self.version
        # you can implement this method here or simply look at the parse()-method where
        # base.add_value('hash', hash_temp)
        # is set manually.
        pass

    def start_requests(self):
        for start_url in self.start_urls:
            yield scrapy.Request(url=start_url, callback=self.parse)

    def parse(self, response: scrapy.http.Response, **kwargs) -> BaseItemLoader:
        base = BaseItemLoader()
        # ALL possible keys for the different Item and ItemLoader-classes can be found inside converter/items.py

        # TODO: fill "base"-keys with values for
        #  - sourceId           required
        #  - hash               required
        #  - lom                required    (see: LomBaseItemLoader below)
        #  - valuespaces        required    (see: ValueSpacesItemLoader below)
        #  - permissions        required    (see: PermissionItemLoader below)
        #  - license            required    (see: LicenseItemLoader below)
        #  - lastModified       recommended
        #  - type               recommended
        #  - thumbnail          recommended
        #  - uuid               optional (please only set this if you actually know the uuid of the internal document)
        #  - collection         optional
        #  - origin             optional
        #  - ranking            optional
        #  - fulltext           optional
        #  - publisher          optional
        #  - notes              optional
        base.add_value('sourceId', response.url)
        # if the source doesn't have a "datePublished" or "lastModified"-value in its header or JSON_LD,
        # you might have to help yourself with a unique string consisting of the datetime of the crawl + self.version
        hash_temp: str = "This string should consist of a date (publication date, preferably)" + self.version
        base.add_value('hash', hash_temp)
        last_modified = None
        base.add_value('lastModified', last_modified)
        # sometimes you might get a "type"-value from the JSON_LD. If it's not supplied by the website you're crawling,
        # you might need to use a constant:
        base.add_value('type', Constants.TYPE_MATERIAL)
        thumbnail_url: str = "This string should hold the thumbnail URL"
        base.add_value('thumbnail', thumbnail_url)

        lom = LomBaseItemloader()
        # TODO: afterwards fill up the LomBaseItem with
        #  - LomGeneralItem                 required
        #  - LomTechnicalItem               required
        #  - LomLifeCycleItem               required (multiple possible)
        #  - LomEducationalItem             required

        general = LomGeneralItemloader()
        # TODO: fill "general"-keys with values for
        #  - identifier                     required
        #  - title                          required
        #  - keyword                        required
        #  - description                    required
        #  - language                       recommended
        #  - coverage                       optional
        #  - structure                      optional
        #  - aggregationLevel               optional
        # e.g.: the unique identifier might be the URL to a material
        general.add_value('identifier', response.url)
        # TODO: don't forget to add key-value-pairs for 'title', 'keyword' and 'description'!
        # once we've added all available values to the necessary keys in our LomGeneralItemLoader,
        # we call the load_item()-method to return a (now filled) LomGeneralItem to the LomBaseItemLoader
        lom.add_value('general', general.load_item())

        technical = LomTechnicalItemLoader()
        # TODO: fill "technical"-keys with values for
        #  - format                         required
        #  - location                       required
        #  - size                           optional
        #  - requirement                    optional
        #  - installationRemarks            optional
        #  - otherPlatformRequirements      optional
        #  - duration                       optional (only applies to audiovisual content like videos/podcasts)
        # similar to how the "general"-LomGeneralItemLoader was filled with Items, individual values can be set with
        # technical.add_value('key','value')
        # or replaced with:
        # technical.replace_value('key', 'value')
        lom.add_value('technical', technical.load_item())

        lifecycle = LomLifecycleItemloader()
        # TODO: fill "lifecycle"-keys with values for
        #  - role                           recommended
        #  - firstName                      recommended
        #  - lastName                       recommended
        #  - url                            recommended
        #  - date                           recommended
        #  - organization                   optional
        #  - email                          optional
        #  - uuid                           optional
        lom.add_value('lifecycle', lifecycle.load_item())

        educational = LomEducationalItemLoader()
        # TODO: fill "educational"-keys with values for
        #  - description                    recommended
        #  - language                       recommended
        #  - interactivityType              optional
        #  - interactivityLevel             optional
        #  - semanticDensity                optional
        #  - typicalAgeRange                optional
        #  - difficulty                     optional
        #  - typicalLearningTime            optional
        lom.add_value('educational', educational.load_item())

        # once you've filled "general", "technical", "lifecycle" and "educational" with values,
        # the LomBaseItem is loaded into the "base"-BaseItemLoader
        base.add_value('lom', lom.load_item())

        vs = ValuespaceItemLoader()
        # TODO: fill "valuespaces"-keys with values for
        #  - discipline                     recommended
        #  - intendedEndUserRole            recommended
        #  - learningResourceType           recommended
        #  - conditionsOfAccess             recommended
        #  - containsAdvertisement          recommended
        #  - price                          recommended
        #  - educationalContext             optional
        #  - sourceContentType              optional
        #  - toolCategory                   optional
        #  - accessibilitySummary           optional
        #  - dataProtectionConformity       optional
        #  - fskRating                      optional
        #  - oer                            optional
        base.add_value('valuespaces', vs.load_item())

        lic = LicenseItemLoader()
        # TODO: fill "license"-keys with values for
        #  - url                            required
        #  - oer                            recommended
        #  - author                         recommended
        #  - internal                       optional
        #  - description                    optional
        #  - expirationDate                 optional (for content that expires, e.g. ÖR-Mediatheken)
        base.add_value('license', lic.load_item())

        # Either fill the PermissionItemLoader manually (not necessary most of the times)
        permissions = PermissionItemLoader()
        # or (preferably) call the inherited getPermissions(response)-method
        #   from converter/spiders/base_classes/lom_base.py by using super().:
        # permissions = super().getPermissions(response)
        # TODO: if necessary, add/replace values for the following "permissions"-keys
        #  - public                         optional
        #  - groups                         optional
        #  - mediacenters                   optional
        #  - autoCreateGroups               optional
        #  - autoCreateMediacenters         optional
        base.add_value('permissions', permissions.load_item())

        # Either fill the ResponseItemLoader manually (not necessary most of the time)
        response_loader = ResponseItemLoader()
        # or (preferably) call the inherited mapResponse(response)-method
        #   from converter/spiders/base_classes/lom_base.py by using super().:
        # response_loader = super().mapResponse(response)
        # TODO: if necessary, add/replace values for the following "response"-keys
        #  - url                            required
        #  - status                         optional
        #  - html                           optional
        #  - text                           optional
        #  - headers                        optional
        #  - cookies                        optional
        #  - har                            optional
        base.add_value('response', response_loader.load_item())

        # once all scrapy.Item are loaded into our "base", we yield the BaseItem by calling the .load_item() method
        yield base.load_item()
