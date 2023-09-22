//
//  Comparison.hpp
//  libmlmodelspec
//
//  Created by Zachary Nation on 3/22/17.
//  Copyright © 2017 Apple. All rights reserved.
//

#include "Format.hpp"

#ifndef Comparison_h
#define Comparison_h

namespace CoreML {
    namespace Specification {
        // comparison operators for Specification types
        
        // model container and metadata/interface
        bool operator==(const Model& a,
                        const Model& b);
        bool operator==(const Metadata& a,
                        const Metadata& b);
        bool operator==(const ModelDescription& a,
                        const ModelDescription& b);
        bool operator==(const FeatureDescription& a,
                        const FeatureDescription& b);
        bool isEquivalent(const FeatureDescription& a,
                          const FeatureDescription& b);
        bool operator==(const FeatureType& a,
                        const FeatureType& b);
        
        // pipelines
        bool operator==(const Pipeline& a,
                        const Pipeline& b);
        bool operator==(const PipelineClassifier& a,
                        const PipelineClassifier& b);
        bool operator==(const PipelineRegressor& a,
                        const PipelineRegressor& b);
        
        // regressors
        bool operator==(const GLMRegressor& a,
                        const GLMRegressor& b);
        bool operator==(const GLMRegressor_DoubleArray& a,
                        const GLMRegressor_DoubleArray& b);
        
        bool operator==(const SupportVectorRegressor& a,
                        const SupportVectorRegressor& b);
        bool operator==(const Kernel& a,
                        const Kernel& b);
        bool operator==(const RBFKernel& a,
                        const RBFKernel& b);
        bool operator==(const PolyKernel& a,
                        const PolyKernel& b);
        bool operator==(const SigmoidKernel& a,
                        const SigmoidKernel& b);
        bool operator==(const Coefficients& a,
                        const Coefficients& b);
        bool operator==(const SparseVector& a,
                        const SparseVector& b);
        bool operator==(const SparseNode& a,
                        const SparseNode& b);
        bool operator==(const DenseVector& a,
                        const DenseVector& b);
        
        bool operator==(const TreeEnsembleRegressor& a,
                        const TreeEnsembleRegressor& b);
        bool operator==(const TreeEnsembleParameters& a,
                        const TreeEnsembleParameters& b);
        bool operator==(const TreeEnsembleParameters_TreeNode& a,
                        const TreeEnsembleParameters_TreeNode& b);
        bool operator==(const TreeEnsembleParameters_TreeNode_EvaluationInfo& a,
                        const TreeEnsembleParameters_TreeNode_EvaluationInfo& b);
        
        bool operator==(const NeuralNetworkRegressor& a,
                        const NeuralNetworkRegressor& b);
        bool operator==(const NeuralNetworkLayer& a,
                        const NeuralNetworkLayer& b);
        bool operator==(const NeuralNetworkPreprocessing& a,
                        const NeuralNetworkPreprocessing& b);
        bool operator==(const NeuralNetworkImageScaler& a,
                        const NeuralNetworkImageScaler& b);
        bool operator==(const NeuralNetworkMeanImage& a,
                        const NeuralNetworkMeanImage& b);

        bool operator==(const BayesianProbitRegressor& a,
                        const BayesianProbitRegressor& b);

        // classifiers
        bool operator==(const GLMClassifier& a,
                        const GLMClassifier& b);
        bool operator==(const GLMClassifier_DoubleArray& a,
                        const GLMClassifier_DoubleArray& b);
        
        bool operator==(const SupportVectorClassifier& a,
                        const SupportVectorClassifier& b);
        bool operator==(const TreeEnsembleClassifier& a,
                        const TreeEnsembleClassifier& b);
        bool operator==(const NeuralNetworkClassifier& a,
                        const NeuralNetworkClassifier& b);
        bool operator==(const KNearestNeighborsClassifier& a,
                        const KNearestNeighborsClassifier& b);
        
        // generic models
        bool operator==(const NeuralNetwork& a,
                        const NeuralNetwork& b);
        bool operator==(const CustomModel& a,
                        const CustomModel& b);
        bool operator==(const LinkedModel& a,
                        const LinkedModel& b);
        bool operator==(const ClassConfidenceThresholding& a,
                        const ClassConfidenceThresholding& b);

        // Apple provided models
        bool operator==(const CoreMLModels::WordTagger& a,
                        const CoreMLModels::WordTagger& b);
        bool operator==(const CoreMLModels::TextClassifier& a,
                        const CoreMLModels::TextClassifier& b);
        bool operator==(const CoreMLModels::Gazetteer& a,
                        const CoreMLModels::Gazetteer& b);
        bool operator==(const CoreMLModels::WordEmbedding& a,
                        const CoreMLModels::WordEmbedding& b);
        bool operator==(const CoreMLModels::VisionFeaturePrint& a,
                        const CoreMLModels::VisionFeaturePrint& b);
        bool operator==(const CoreMLModels::AudioFeaturePrint& a,
                        const CoreMLModels::AudioFeaturePrint& b);

        bool operator==(const CoreMLModels::SoundAnalysisPreprocessing& a,
                        const CoreMLModels::SoundAnalysisPreprocessing& b);
        
        // feature engineering
        bool operator==(const OneHotEncoder& a,
                        const OneHotEncoder& b);
        bool operator==(const Imputer& a,
                        const Imputer& b);
        bool operator==(const FeatureVectorizer& a,
                        const FeatureVectorizer& b);
        bool operator==(const FeatureVectorizer_InputColumn& a,
                        const FeatureVectorizer_InputColumn& b);
        bool operator==(const DictVectorizer& a,
                        const DictVectorizer& b);
        bool operator==(const Scaler& a,
                        const Scaler& b);
        bool operator==(const NonMaximumSuppression& a,
                        const NonMaximumSuppression& b);
        bool operator==(const CategoricalMapping& a,
                        const CategoricalMapping& b);
        bool operator==(const Normalizer& a,
                        const Normalizer& b);
        bool operator==(const ArrayFeatureExtractor& a,
                        const ArrayFeatureExtractor& b);
        
        // recommenders
        bool operator==(const ItemSimilarityRecommender& a,
                        const ItemSimilarityRecommender& b);

        // data structures
        
        bool operator==(const Int64Vector& a,
                        const Int64Vector& b);
        bool operator==(const StringVector& a,
                        const StringVector& b);
        bool operator==(const DoubleVector& a,
                        const DoubleVector& b);
        bool operator==(const StringToInt64Map& a,
                        const StringToInt64Map& b);
        bool operator==(const Int64ToStringMap& a,
                        const Int64ToStringMap& b);
        bool operator==(const StringToDoubleMap& a,
                        const StringToDoubleMap& b);
        bool operator==(const Int64ToDoubleMap& a,
                        const Int64ToDoubleMap& b);
        
        
        // comparison of repeated/contained types
        
        template<typename T>
        bool operator==(const ::google::protobuf::RepeatedPtrField<T>& a,
                        const ::google::protobuf::RepeatedPtrField<T>& b) {
            if (a.size() != b.size()) {
                return false;
            }
            for (int i=0; i<a.size(); i++) {
                if (a[i] != b[i]) {
                    return false;
                }
            }
            return true;
        }
        
        template<typename T>
        bool operator==(const ::google::protobuf::RepeatedField<T>& a,
                        const ::google::protobuf::RepeatedField<T>& b) {
            if (a.size() != b.size()) {
                return false;
            }
            for (int i=0; i<a.size(); i++) {
                if (a[i] != b[i]) {
                    return false;
                }
            }
            return true;
        }
        
        // comparison of Map contained types
        template<typename T, typename U>
        bool operator==(const ::google::protobuf::Map<T,U>& a,
                        const ::google::protobuf::Map<T,U>& b) {
            if (a.size() != b.size()) {
                return false;
            }
            for (const auto& pair : a) {
                if (b.find(pair.first) == b.end()) {
                    return false;
                }
                if (b.at(pair.first) != pair.second) {
                    return false;
                }
            }
            return true;
        }

 //
 // Type-specific operator!= overloads necessitated by rdar://98724060 ([libcxx release blocker] Failed to build CoreML_tests (unconstrained operator!=))
 //
        bool operator!=(const ::CoreML::Specification::StringVector& a,
                        const ::CoreML::Specification::StringVector& b);

        bool operator!=(const ::CoreML::Specification::Int64Vector& a,
                        const ::CoreML::Specification::Int64Vector& b);

        bool operator!=(const ::google::protobuf::RepeatedField<::google::protobuf::int32>& a,
                        const ::google::protobuf::RepeatedField<::google::protobuf::int32>& b);

        bool operator!=(const ::google::protobuf::RepeatedField<float>& a,
                        const ::google::protobuf::RepeatedField<float>& b);

        bool operator!=(const ::google::protobuf::RepeatedField<double>& a,
                        const ::google::protobuf::RepeatedField<double>& b);

        bool operator!=(const ::CoreML::Specification::Model& a,
                        const ::CoreML::Specification::Model& b);

        bool operator!=(const ::CoreML::Specification::ModelDescription& a,
                        const ::CoreML::Specification::ModelDescription& b);

        bool operator!=(const ::CoreML::Specification::Metadata& a,
                        const ::CoreML::Specification::Metadata& b);

        bool operator!=(const ::CoreML::Specification::FeatureType& a,
                        const ::CoreML::Specification::FeatureType& b);

        bool operator!=(const ::CoreML::Specification::Kernel& a,
                        const ::CoreML::Specification::Kernel& b);

        bool operator!=(const ::CoreML::Specification::Coefficients& a,
                        const ::CoreML::Specification::Coefficients& b);

        bool operator!=(const ::CoreML::Specification::TreeEnsembleParameters& a,
                        const ::CoreML::Specification::TreeEnsembleParameters& b);

        bool operator!=(const ::google::protobuf::RepeatedPtrField<::CoreML::Specification::FeatureDescription>& a,
                        const ::google::protobuf::RepeatedPtrField<::CoreML::Specification::FeatureDescription>& b);

        bool operator!=(const ::google::protobuf::RepeatedPtrField<::CoreML::Specification::GLMRegressor_DoubleArray>& a,
                        const ::google::protobuf::RepeatedPtrField<::CoreML::Specification::GLMRegressor_DoubleArray>& b);

        bool operator!=(const ::google::protobuf::RepeatedPtrField<::CoreML::Specification::GLMClassifier_DoubleArray>& a,
                        const ::google::protobuf::RepeatedPtrField<::CoreML::Specification::GLMClassifier_DoubleArray>& b);

        bool operator!=(const ::google::protobuf::RepeatedPtrField<::CoreML::Specification::TreeEnsembleParameters_TreeNode>& a,
                        const ::google::protobuf::RepeatedPtrField<::CoreML::Specification::TreeEnsembleParameters_TreeNode>& b);

        bool operator!=(const ::google::protobuf::RepeatedPtrField<::CoreML::Specification::NeuralNetworkLayer>& a,
                        const ::google::protobuf::RepeatedPtrField<::CoreML::Specification::NeuralNetworkLayer>& b);

        bool operator!=(const ::google::protobuf::RepeatedPtrField<::CoreML::Specification::TreeEnsembleParameters_TreeNode_EvaluationInfo>& a,
                        const ::google::protobuf::RepeatedPtrField<::CoreML::Specification::TreeEnsembleParameters_TreeNode_EvaluationInfo>& b);

        bool operator!=(const ::google::protobuf::RepeatedPtrField< ::CoreML::Specification::NeuralNetworkPreprocessing>& a,
                        const ::google::protobuf::RepeatedPtrField< ::CoreML::Specification::NeuralNetworkPreprocessing>& b);

        bool operator!=(const ::google::protobuf::RepeatedPtrField< ::CoreML::Specification::Coefficients>& a,
                        const ::google::protobuf::RepeatedPtrField< ::CoreML::Specification::Coefficients>& b);

        bool operator!=(const ::google::protobuf::RepeatedPtrField< ::CoreML::Specification::SparseVector>& a,
                        const ::google::protobuf::RepeatedPtrField< ::CoreML::Specification::SparseVector>& b);

        bool operator!=(const ::google::protobuf::RepeatedPtrField< ::CoreML::Specification::DenseVector>& a,
                        const ::google::protobuf::RepeatedPtrField< ::CoreML::Specification::DenseVector>& b);

        bool operator!=(const ::google::protobuf::Map<::std::string, ::std::string>& a,
                        const ::google::protobuf::Map<::std::string, ::std::string>& b);

        bool operator!=(const CoreML::Specification::SparseVector& a,
                        const CoreML::Specification::SparseVector& b);

        bool operator!=(const CoreML::Specification::SparseNode& a,
                        const CoreML::Specification::SparseNode& b);

        bool operator!=(const CoreML::Specification::DenseVector& a,
                        const CoreML::Specification::DenseVector& b);

        bool operator!=(const CoreML::Specification::FeatureVectorizer_InputColumn& a,
                        const CoreML::Specification::FeatureVectorizer_InputColumn& b);

        bool operator!=(const CoreML::Specification::FeatureDescription& a,
                        const CoreML::Specification::FeatureDescription& b);

        bool operator!=(const CoreML::Specification::GLMRegressor_DoubleArray& a,
                        const CoreML::Specification::GLMRegressor_DoubleArray& b);

        bool operator!=(const CoreML::Specification::GLMClassifier_DoubleArray& a,
                        const CoreML::Specification::GLMClassifier_DoubleArray& b);

        bool operator!=(const CoreML::Specification::TreeEnsembleParameters_TreeNode& a,
                        const CoreML::Specification::TreeEnsembleParameters_TreeNode& b);

        bool operator!=(const CoreML::Specification::TreeEnsembleParameters_TreeNode_EvaluationInfo& a,
                        const CoreML::Specification::TreeEnsembleParameters_TreeNode_EvaluationInfo& b);

        bool operator!=(const CoreML::Specification::NeuralNetworkLayer& a,
                        const CoreML::Specification::NeuralNetworkLayer& b);

        bool operator!=(const CoreML::Specification::NeuralNetworkPreprocessing& a,
                        const CoreML::Specification::NeuralNetworkPreprocessing& b);

    }
}

#endif /* Comparison_h */
